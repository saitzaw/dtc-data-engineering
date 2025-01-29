
variable "project" {
  description = "The GCP project ID"
  type        = string
  default     = "gcp-terraform-sthz"

}

variable "credentials" {
  description = "The path to the GCP credentials file"
  type        = string
  default     = "./keys/my-certs.json"

}

variable "region" {
  description = "The region of the resources"
  type        = string
  default     = "asia-southeast1"

}

variable "location" {
  description = "The location/region of the resources"
  type        = string
  default     = "asia-southeast1"
}

variable "bq_dataset_name" {
  description = "The name of the BigQuery dataset"
  type        = string
  default     = "demo_dataset"

}

variable "gcp_bucket_name" {
  description = "The name of the BigQuery dataset"
  type        = string
  default     = "gcp-terraform-sthz-demo-bucket-1111"

}

variable "gcp_storage_class" {
  description = "The name of GCP storage bucket"
  type        = string
  default     = "STANDARD"
}