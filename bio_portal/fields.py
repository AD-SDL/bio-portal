from urllib.parse import urlsplit, urlunsplit, urlencode
import re

def title(result):
    if not result[0]["dc"]:
        return
    t = result[0]['dc']['titles'][0]["title"]
    return t
    if not ("experiment" in t):
        """The title for this Globus Search subject"""
        return result[0]["dc"]["titles"][0]["title"]
    return result[0]["project_metadata"]["experiment"]

def all_files(result):
    new_files = []
    for file in result[0]["files"]:
        url = file.get("url")
        path = urlsplit(url).path
        new_url = urlunsplit(("https", "g-cd34a.fd635.8443.data.globus.org", path, "", ""))
        new_files.append(new_url)
    return new_files

def chart(result):
    fs = {}
    for f in all_files(result):
        if re.match(".*\.png", f):
            fs[f.split('/')[-1]] = f
    return fs

def pictures(result):
    fs = []
    for f in all_files(result):
        if re.match(".*\.png", f):
            fs = [f] + fs    
    return fs

def real_plates(result):
    fs = []
    for f in all_files(result):
        if re.match(".*real_plate.\.png", f):
          fs = [f] + fs
    return fs

def target_color(result):
    fs = {}
    for f in all_files(result):
        if re.match(".*target_color\.png", f):
          return f    
    return fs

def best_color(result):
    fs = {}
    for f in all_files(result):        
        if re.match(".*best_color\.png", f):
            return f
    return fs

def final_img(result):
    fs = {}
    for f in all_files(result):
           if re.match(".*final_image.jpg", f):
               return f
    return fs

def results(result):
    return result[0]

def exp_type(result):
    if "exp_type" in result[0]["project_metadata"]:
       return result[0]["project_metadata"]["exp_type"]
    return "tests"
