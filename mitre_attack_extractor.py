import requests
import json
import os
import yaml
import re

def sanitize_filename(filename):
    """
    Sanitize the filename to remove invalid characters and limit length
    """
    # Replace spaces and special characters with underscores
    filename = re.sub(r'[^\w\-_\. ]', '_', filename)
    # Replace multiple consecutive spaces/underscores with a single underscore
    filename = re.sub(r'[\s_]+', '_', filename)
    # Trim to a reasonable length
    filename = filename[:100]
    # Ensure it doesn't end with a period or space
    filename = filename.strip('. ')
    return filename

def fetch_attack_data():
    """
    Fetch the latest ATT&CK Enterprise tactics and techniques from MITRE's JSON source
    """
    url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching ATT&CK data: {e}")
        return None

def parse_taxi_info(attack_data):
    """
    Extract STIX/Taxi information from the ATT&CK JSON data
    """
    techniques = []
    for obj in attack_data.get('objects', []):
        if obj.get('type') == 'attack-pattern':
            # Extract additional metadata
            technique_info = {
                'id': obj.get('id', 'N/A'),
                'name': obj.get('name', 'N/A'),
                'description': obj.get('description', 'No description available'),
                'external_references': obj.get('external_references', []),
                'kill_chain_phases': obj.get('kill_chain_phases', []),
                'platforms': obj.get('x_mitre_platforms', []),
                'tactics': [],
                'data_sources': obj.get('x_mitre_data_sources', []),
                'contributors': obj.get('x_mitre_contributors', []),
                'detection': obj.get('x_mitre_detection', 'No detection information available'),
                'permissions_required': obj.get('x_mitre_permissions_required', []),
                'system_requirements': obj.get('x_mitre_system_requirements', [])
            }
            
            # Extract tactics
            for ref in obj.get('external_references', []):
                if ref.get('source_name') == 'mitre-attack':
                    technique_info['mitre_attack_url'] = ref.get('url', '')
            
            # Extract tactic names
            for kill_chain in technique_info['kill_chain_phases']:
                if kill_chain.get('kill_chain_name') == 'mitre-attack':
                    tactic = kill_chain.get('phase_name', '')
                    if tactic and tactic not in technique_info['tactics']:
                        technique_info['tactics'].append(tactic)
            
            techniques.append(technique_info)
    return techniques

def create_markdown_files(techniques, output_dir='Mitre_ATT&CK_Techniques'):
    """
    Create markdown files for each technique in Obsidian-friendly format with custom title
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for technique in techniques:
        # Prepare tactics string (use first tactic if multiple)
        primary_tactic = technique['tactics'][0] if technique['tactics'] else 'Unknown_Tactic'
        
        # Create custom title
        custom_title = f"{primary_tactic} - {technique['name']}"
        
        # Create filename using technique ID, sanitized custom title
        filename = f"{technique['id']}_{sanitize_filename(custom_title)}.md"
        filepath = os.path.join(output_dir, filename)

        # Prepare YAML front matter
        properties = {
            'title': custom_title,
            'id': technique['id'],
            'name': technique['name'],
            'tactics': technique['tactics'],
            'platforms': technique['platforms'],
            'data_sources': technique['data_sources'],
            'contributors': technique['contributors'],
            'mitre_attack_url': technique.get('mitre_attack_url', '')
        }

        # Remove empty lists and None values
        properties = {k: v for k, v in properties.items() if v}

        # Prepare markdown content
        markdown_content = "---\n"
        markdown_content += yaml.safe_dump(properties, default_flow_style=False)
        markdown_content += "---\n\n"

        # Add technical details table
        markdown_content += "## Technical Details\n\n"
        markdown_content += "| Attribute | Details |\n"
        markdown_content += "|-----------|----------|\n"
        
        # Add detailed technical information to the table
        if technique['tactics']:
            markdown_content += f"| **Tactics** | {', '.join(technique['tactics'])} |\n"
        
        if technique['platforms']:
            markdown_content += f"| **Platforms** | {', '.join(technique['platforms'])} |\n"
        
        if technique['data_sources']:
            markdown_content += f"| **Data Sources** | {', '.join(technique['data_sources'])} |\n"
        
        if technique['permissions_required']:
            markdown_content += f"| **Permissions Required** | {', '.join(technique['permissions_required'])} |\n"
        
        if technique['system_requirements']:
            markdown_content += f"| **System Requirements** | {', '.join(technique['system_requirements'])} |\n"
        
        markdown_content += f"| **MITRE ATT&CK URL** | [{technique.get('mitre_attack_url', 'N/A')}]({technique.get('mitre_attack_url', '')}) |\n\n"

        # Add main content sections
        markdown_content += f"# {technique['name']} ({technique['id']})\n\n"
        markdown_content += f"## Description\n{technique['description']}\n\n"

        # Add detection information
        if technique['detection'] and technique['detection'] != 'No detection information available':
            markdown_content += "## Detection\n"
            markdown_content += f"{technique['detection']}\n\n"

        # Add external references
        markdown_content += "## External References\n"
        for ref in technique['external_references']:
            if 'url' in ref:
                markdown_content += f"- [{ref.get('source_name', 'Reference')}]({ref['url']})\n"

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

def main():
    # Fetch ATT&CK data
    attack_data = fetch_attack_data()
    
    if attack_data:
        # Parse techniques
        techniques = parse_taxi_info(attack_data)
        
        # Create markdown files
        create_markdown_files(techniques)
        
        print(f"Created markdown files for {len(techniques)} techniques")

if __name__ == "__main__":
    main()