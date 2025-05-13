# ☁️ AWS CLI Python Scripts

This repository contains a collection of **Python scripts** that use the **AWS CLI** and **boto3 SDK** to automate common AWS tasks. These scripts are designed for convenience, learning, and real-world AWS operations.

---

## 📂 Scripts Included

| Script | Description |
|--------|-------------|
| `list_ec2_instances.py` | Lists all EC2 instances with their status and public IPs |
| `s3_bucket_backup.py`   | Syncs local directory to S3 (backup) |
| `launch_instance.py`    | Launches an EC2 instance with predefined settings |
| `terminate_instance.py` | Terminates a given EC2 instance |
| `list_iam_users.py`     | Displays all IAM users and their creation dates |

---

## 📦 Requirements

- Python 3.7+
- `boto3` library
- AWS CLI (configured with credentials)

Install dependencies:
```bash
pip install boto3
