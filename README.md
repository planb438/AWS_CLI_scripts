[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Ubuntu%2022.04%2B-lightgrey)](#)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-MicroK8s%20%7C%20kubeadm-blue)](#)
[![YouTube](https://img.shields.io/badge/YouTube-TechShorts-red)](https://www.youtube.com/@adaribain)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Adari%20Bain-blue)](https://www.linkedin.com/in/adari-bain-298924152/)


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
