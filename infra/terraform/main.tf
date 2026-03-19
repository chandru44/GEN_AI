terraform {
  required_version = ">= 1.6.0"
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  default = "us-east-1"
}

resource "aws_s3_bucket" "frontend_bucket" {
  bucket = "soc-copilot-v2-frontend-demo"
}
