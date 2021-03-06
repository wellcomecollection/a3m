"""Shared directory setup.
"""
import logging
import os

from django.conf import settings


logger = logging.getLogger(__name__)


DEFAULT_PROCESSING_CONFIG = """<processingMCP>
  <preconfiguredChoices>
    <!-- Select compression level -->
    <preconfiguredChoice>
      <appliesTo>01c651cb-c174-4ba4-b985-1d87a44d6754</appliesTo>
      <goToChain>414da421-b83f-4648-895f-a34840e3c3f5</goToChain>
    </preconfiguredChoice>
    <!-- Examine contents -->
    <preconfiguredChoice>
      <appliesTo>accea2bf-ba74-4a3a-bb97-614775c74459</appliesTo>
      <goToChain>e0a39199-c62a-4a2f-98de-e9d1116460a8</goToChain>
    </preconfiguredChoice>
    <!-- Perform file format identification (Submission documentation & metadata) -->
    <preconfiguredChoice>
      <appliesTo>087d27be-c719-47d8-9bbb-9a7d8b609c44</appliesTo>
      <goToChain>4dec164b-79b0-4459-8505-8095af9655b5</goToChain>
    </preconfiguredChoice>
    <!-- Normalize (match 1 for "Normalize for preservation") -->
    <preconfiguredChoice>
      <appliesTo>cb8e5706-e73f-472f-ad9b-d1236af8095f</appliesTo>
      <goToChain>612e3609-ce9a-4df6-a9a3-63d634d2d934</goToChain>
    </preconfiguredChoice>
    <!-- Normalize (match 2 for "Normalize for preservation") -->
    <preconfiguredChoice>
      <appliesTo>7509e7dc-1e1b-4dce-8d21-e130515fce73</appliesTo>
      <goToChain>612e3609-ce9a-4df6-a9a3-63d634d2d934</goToChain>
    </preconfiguredChoice>
    <!-- Bind PIDs -->
    <preconfiguredChoice>
      <appliesTo>a2ba5278-459a-4638-92d9-38eb1588717d</appliesTo>
      <goToChain>44a7c397-8187-4fd2-b8f7-c61737c4df49</goToChain>
    </preconfiguredChoice>
    <!-- Delete packages after extraction -->
    <preconfiguredChoice>
      <appliesTo>f19926dd-8fb5-4c79-8ade-c83f61f55b40</appliesTo>
      <goToChain>85b1e45d-8f98-4cae-8336-72f40e12cbef</goToChain>
    </preconfiguredChoice>
    <!-- Transcribe files (OCR) -->
    <preconfiguredChoice>
      <appliesTo>82ee9ad2-2c74-4c7c-853e-e4eaf68fc8b6</appliesTo>
      <goToChain>0a24787c-00e3-4710-b324-90e792bfb484</goToChain>
    </preconfiguredChoice>
    <!-- Perform file format identification (Transfer) -->
    <preconfiguredChoice>
      <appliesTo>f09847c2-ee51-429a-9478-a860477f6b8d</appliesTo>
      <goToChain>d97297c7-2b49-4cfe-8c9f-0613d63ed763</goToChain>
    </preconfiguredChoice>
    <!-- Generate transfer structure report -->
    <preconfiguredChoice>
      <appliesTo>56eebd45-5600-4768-a8c2-ec0114555a3d</appliesTo>
      <goToChain>df54fec1-dae1-4ea6-8d17-a839ee7ac4a7</goToChain>
    </preconfiguredChoice>
    <!-- Perform policy checks on originals -->
    <preconfiguredChoice>
      <appliesTo>70fc7040-d4fb-4d19-a0e6-792387ca1006</appliesTo>
      <goToChain>3e891cc4-39d2-4989-a001-5107a009a223</goToChain>
    </preconfiguredChoice>
    <!-- Generate thumbnails -->
    <preconfiguredChoice>
      <appliesTo>498f7a6d-1b8c-431a-aa5d-83f14f3c5e65</appliesTo>
      <goToChain>972fce6c-52c8-4c00-99b9-d6814e377974</goToChain>
    </preconfiguredChoice>
    <!-- Select compression algorithm -->
    <preconfiguredChoice>
      <appliesTo>01d64f58-8295-4b7b-9cab-8f1b153a504f</appliesTo>
      <goToChain>9475447c-9889-430c-9477-6287a9574c5b</goToChain>
    </preconfiguredChoice>
    <!-- Perform policy checks on access derivatives -->
    <preconfiguredChoice>
      <appliesTo>8ce07e94-6130-4987-96f0-2399ad45c5c2</appliesTo>
      <goToChain>76befd52-14c3-44f9-838f-15a4e01624b0</goToChain>
    </preconfiguredChoice>
    <!-- Perform file format identification (Ingest) -->
    <preconfiguredChoice>
      <appliesTo>7a024896-c4f7-4808-a240-44c87c762bc5</appliesTo>
      <goToChain>5b3c8268-5b33-4b70-b1aa-0e4540fe03d1</goToChain>
    </preconfiguredChoice>
    <!-- Perform policy checks on preservation derivatives -->
    <preconfiguredChoice>
      <appliesTo>153c5f41-3cfb-47ba-9150-2dd44ebc27df</appliesTo>
      <goToChain>b7ce05f0-9d94-4b3e-86cc-d4b2c6dba546</goToChain>
    </preconfiguredChoice>
    <!-- Assign UUIDs to directories -->
    <preconfiguredChoice>
      <appliesTo>bd899573-694e-4d33-8c9b-df0af802437d</appliesTo>
      <goToChain>2dc3f487-e4b0-4e07-a4b3-6216ed24ca14</goToChain>
    </preconfiguredChoice>
    <!-- Document empty directories -->
    <preconfiguredChoice>
      <appliesTo>d0dfa5fc-e3c2-4638-9eda-f96eea1070e0</appliesTo>
      <goToChain>65273f18-5b4e-4944-af4f-09be175a88e8</goToChain>
    </preconfiguredChoice>
    <!-- Extract packages -->
    <preconfiguredChoice>
      <appliesTo>dec97e3c-5598-4b99-b26e-f87a435a6b7f</appliesTo>
      <goToChain>01d80b27-4ad1-4bd1-8f8d-f819f18bf685</goToChain>
    </preconfiguredChoice>
  </preconfiguredChoices>
</processingMCP>
"""
BUILTIN_CONFIGS = {"default": DEFAULT_PROCESSING_CONFIG}


def install_builtin_config(name):
    """
    Install the original version of a builtin processing configuration
    """
    config = BUILTIN_CONFIGS[name]
    path = os.path.join(settings.SHARED_DIRECTORY, "processingConfigs", f"{name}.xml")
    if not os.path.isfile(path):
        with open(path, "w") as file_descriptor:
            file_descriptor.write(config)

    return config


def create():
    dirs = (
        "currentlyProcessing/transfer",
        "currentlyProcessing/ingest",
        "completed",
        "failed",
        "policies",
        "processingConfigs",
        "tmp",
    )
    for dirname in dirs:
        dirname = os.path.join(settings.SHARED_DIRECTORY, dirname)
        if os.path.isdir(dirname):
            continue
        logger.debug("Creating directory: %s", dirname)
        os.makedirs(dirname, mode=0o770)

    # Populate processing configurations
    for config in BUILTIN_CONFIGS:
        install_builtin_config(config)
