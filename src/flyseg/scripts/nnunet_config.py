import os
import zipfile
import gdown
import shutil

# === 路径配置 ===
from pathlib import Path
MODEL_DIR = str(Path.home() / ".flyseg" / "pretrained_model")
MODEL_ZIP = os.path.join(MODEL_DIR, "pretrained_model.zip")

NNUNET_BASE = os.path.join(MODEL_DIR, "pretrained_model", "nnUNet")
NNUNET_RESULTS = os.path.join(NNUNET_BASE, "nnUNet_results")
NNUNET_RAW = os.path.join(NNUNET_BASE, "nnUNet_raw")
NNUNET_PREPROCESSED = os.path.join(NNUNET_BASE, "nnUNet_preprocessed")

MODEL_URL = "https://drive.google.com/file/d/1ercpkWgHcYTDSsbke-YkYugSslSB6dUl/view?usp=drive_link"

# === 工具函数 ===
def is_unc(path: str) -> bool:
    return path.startswith("\\\\") or path.startswith("//")

def ensure_model_downloaded():
    """
    下载并解压预训练模型，如果本地不存在。
    """
    os.makedirs(MODEL_DIR, exist_ok=True)

    if not any(fname.endswith(".pkl") or os.path.isdir(os.path.join(MODEL_DIR, fname)) for fname in os.listdir(MODEL_DIR)):
        print("🧠 pretrained_model not found, downloading...")

        print("⬇️ Downloading model from Google Drive...")
        gdown.download(MODEL_URL, MODEL_ZIP, quiet=False, fuzzy=True)

        # print("📦 Extracting model...")
        with zipfile.ZipFile(MODEL_ZIP, "r") as zip_ref:
            zip_ref.extractall(MODEL_DIR)

        print("✅ Model downloaded and extracted.")
        if os.path.exists(MODEL_ZIP):
            os.remove(MODEL_ZIP)
    else:
        print("✅ Pretrained model found.")

def configure_nnunet_environment():
    """
    设置 nnUNet 所需的环境变量（基于本地模型结构）
    """
    if not os.path.isdir(NNUNET_RESULTS):
        raise FileNotFoundError(f"❌ nnUNet results directory not found: {NNUNET_RESULTS}")

    os.environ["nnUNet_results"] = NNUNET_RESULTS
    os.environ["nnUNet_raw"] = NNUNET_RAW
    os.environ["nnUNet_preprocessed"] = NNUNET_PREPROCESSED

    # print("✅ nnUNet environment configured:")
    # print(f"  nnUNet_results      = {NNUNET_RESULTS}")
    # print(f"  nnUNet_raw          = {NNUNET_RAW}")
    # print(f"  nnUNet_preprocessed = {NNUNET_PREPROCESSED}")

    return NNUNET_RAW, NNUNET_RESULTS

def clean_model_cache():
    if os.path.exists(MODEL_DIR):
        shutil.rmtree(MODEL_DIR)
        print("🧹 Deleted pretrained_model folder.")
