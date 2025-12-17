import kagglehub

if __name__ == "__main__":
    #kagglehub.login()

    # Download latest version
    path = kagglehub.dataset_download("nexuswho/aitex-fabric-image-database")

    print("Path to dataset files:", path)