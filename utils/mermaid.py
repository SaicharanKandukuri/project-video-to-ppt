from utils.utils import Popen

def mermaidImage(mmdFile: str, out="out.svg"):
    """Convert a mermaid file to an image

    Args:
        mmdFile (str): The mermaid file
        out (str, optional): The output file. Defaults to "out.svg".
    """
    Popen(["mmdc", "-i", mmdFile, "-o", out])