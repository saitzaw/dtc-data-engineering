terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.18.0"
    }
  }
}

provider "google" {
  project = "gcp-terraform-sthz"
  region  = "asia-southeast1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "gcp-terraform-sthz-demo-bucket-1111"
  location      = "asia-southeast1"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3
    }
    action {
      type = "Delete"
    }
  }

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}