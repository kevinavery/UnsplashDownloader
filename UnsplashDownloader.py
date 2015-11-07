import urllib;
import os,sys,re,logging,chromalog;
from chromalog.mark.helpers.simple import success, error, important

chromalog.basicConfig(level=logging.INFO,format="[%(levelname)s] %(message)s");
logger = logging.getLogger(__name__);

isEnd = False;
url = "";
content = "";
pattern = "<a href=\"/photos/(.*?)\"";

directory = os.path.realpath(os.getcwd() + "\\pictures\\");

page  = 1;
count = 0;
if not os.path.exists(directory):
    logger.info("Creating directory");
    os.makedirs(directory);

while (not isEnd):
    isEnd = True;
    url = "http://unsplash.com/?page=" + str(page);
    content = urllib.urlopen(url).read();
    for s in re.findall(pattern,content):
        pic = "http://unsplash.com/photos/" + s + "/download";
        filename = directory+ "\\" + s + ".jpeg";
        logger.info("Loading:\t %s",s)
        if(not os.path.exists(filename)):
            urllib.urlretrieve(pic,filename);

            logger.info("Loaded:\t %s (%d)",success(s),count);

            count+=1;
            isEnd = False;
        else:

            logger.warning(s + " Exists");

    page+=1;
logger.info("%s %d %s",success("Successfully downloaded"),count,success("pictures"));
