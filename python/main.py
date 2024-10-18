import sys
sys.path.append('./src')

from directory import Directory
from home import Home
from sidebar import Sidebar

print('==================== Categosizing the Entire aya-issues Wiki pages... ====================')
Directory().run
Home().run
Sidebar().run
print('==================== Done categorising the Entire aya-issues Wiki pages 🎉 ====================')
