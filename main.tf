provider "google" {
  project     = "ensai-2024"
  region      = "europe-west1"
  zone        = "europe-west1-b"
  credentials = "ensai-2024-37c511689d57.json"
}


resource "google_compute_instance" "prediction-api-trang" {
  name         = "prediction-api-trang"
  machine_type = "e2-standard-2"
  zone         = "europe-west1-b"
  metadata_startup_script = file("startup_script.sh")

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }
}
