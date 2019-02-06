#!/anaconda/envs/py36server/bin/python
import sys
sys.path.append('/anaconda/envs/py36server/bin/python')
sys.path.insert(0,"/datadrive/123/ProjectsWebServer/MyFlaskBackEnd/TextSummarization/Server")
from restserver import app as application