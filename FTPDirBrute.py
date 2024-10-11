import ftplib
from tqdm import tqdm

def connect_to_ftp(server, username, password, dirs_file):
    try:
        ftp = ftplib.FTP(server)
        ftp.login(user=username, passwd=password)
        print(f"Connected to {server}")

        with open(dirs_file, 'r') as f:
            dirs = f.read().splitlines()

        with tqdm(total=len(dirs), desc="Creating directories") as progress_bar:
            for ftp_dir in dirs:
                try:
                    ftp.mkd(ftp_dir)
                except ftplib.error_perm as e:
                    if str(e).startswith("550"):
                        print(f"Alert: Dir {ftp_dir} found!")
                    else:
                        print(f"Failed to create {ftp_dir}: {e}")
                progress_bar.update(1)

        ftp.quit()
        print("Connection closed.")

    except ftplib.all_errors as e:
        print(f"FTP error: {e}")
    except FileNotFoundError:
        print(f"File {dirs_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    server = "IP.ADDR"  # Replace with your FTP server
    username = "anonymous"  # Replace with your username
    password = ""  # Replace with your password

    dirs_file = "directory-list-2.3-big.txt"  # Replace with the path to your dir file

    connect_to_ftp(server, username, password, dirs_file)
