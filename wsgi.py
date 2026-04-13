import sys
import os
project_home = '/home/yourusername/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path
from app_meupresente import app as application
