Scientific Calculator
This project is a Python-based scientific calculator with fastAPI, packaged for easy deployment using Docker and Ansible.

Features
    Scientific calculations (trigonometry, logarithms, etc.)
    REST API for programmatic access
    Unit tests for reliability
    Dockerized for easy deployment
    Automated deployment with Ansible
    Getting Started
    Python 3.12
    Docker
    Ansibl


Setup & Run Locally
Clone the repository:
''' git clone https://github.com/Nikhilesh611/SPE_Mini_Project.git '''
''' cd SPE_Mini_Project '''

Set up Python environment:
    '''python3 -m venv .venv''' 
    ''' . .venv/bin/activate'''   # On Windows: .venv\Scripts\activate
    ''' pip install --upgrade pip''' 
    ''' pip install -e .''' 
   '''  pip install -r requirements.txt''' 


Run unit tests:
    ''' python -m unittest discover tests''' 
Build Docker image:
    ''' docker build -t nikhilesh611/scientific_calculator .''' 
Run Docker container:
    ''' docker run -p 5000:5000 nikhilesh611/scientific_calculator''' 
Deployment with Ansible
    Configure your hosts in hosts.ini.
    Run the playbook:
        ''' ansible-playbook -i ansible/hosts.ini ansible/deploy.yml''' 
