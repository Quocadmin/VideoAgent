import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'tools/CosyVoice'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools/CosyVoice/third_party/Matcha-TTS'))

logging.basicConfig(level=logging.WARNING)  # 或 logging.ERROR
logging.getLogger("modelscope").setLevel(logging.WARNING)
from environment.agents.multi import MultiAgent

def main():
    multi_agent = MultiAgent()
    multi_agent.run()

if __name__ == "__main__":
    main()