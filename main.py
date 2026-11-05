import hashlib
import io

def compute_hashes(stream: io.BytesIO) -> dict[str, str]:
    sha = hashlib.sha256()
    md5 = hashlib.md5()
    while chunk := stream.read(8192):
        sha.update(chunk)
        md5.update(chunk)
    return {"sha256": sha.hexdigest(), "md5": md5.hexdigest()}

if __name__ == '__main__':
    data = io.BytesIO(b"Autonomous hourly project checksum test")
    hashes = compute_hashes(data)
    print("Computed Hashes:", hashes)
    assert len(hashes["sha256"]) == 64
