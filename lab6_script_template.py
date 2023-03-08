import requests
import hashlib
import os
import subprocess

def main():

    # Get the expected SHA-256 hash value of the VLC installer
    expected_sha256 = get_expected_sha256()

    # Download (but don't save) the VLC installer from the VLC website
    installer_data = download_installer()

    # Verify the integrity of the downloaded VLC installer by comparing the
    # expected and computed SHA-256 hash values
    if installer_ok(installer_data, expected_sha256):

        # Save the downloaded VLC installer to disk
        installer_path = save_installer(installer_data)

        # Silently run the VLC installer
        run_installer(installer_path)

        # Delete the VLC installer from disk
        delete_installer(installer_path)

def get_expected_sha256():
     # Calculating the hash value
    image_hash = hashlib.sha256(file_url).hexdigest()    
    return image_hash
             

def download_installer():
    # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe.sha256'
    resp_msg = requests.get(file_url)

    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:

        # Extract binary file content from response message
        return  resp_msg.content

        
def installer_ok(installer_data, expected_sha256):
     # Send GET message to download the file
    file_url = 'http://download.videolan.org/pub/videolan/vlc/3.0.17.4/win64/vlc-3.0.17.4-win64.exe'
    resp_msg = requests.get(file_url)

    # Check whether the download was successful
    if resp_msg.status_code == requests.codes.ok:

        # Extract binary file content from response message
        return  resp_msg.content


def save_installer(installer_data):
    with open(r'C:\temp', 'wb') as file:
        file.write(file_url)         
        return

def run_installer(installer_path):
     # running the VLC installer
        run_installer = r'C:\temp\vlc.exe'
        subprocess.run([run_installer, '/L=1033', '/S'])

    
def delete_installer(installer_path):
     # Deleting VLC installer 
        run_installer = r'C:\temp\vlc.exe'
        os.remove(run_installer)
             


main()
main()
