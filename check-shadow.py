from __future__ import print_function
import apt_pkg
import json

# init the package system
apt_pkg.init()
cache = apt_pkg.Cache()
ads1 = {}
for i,pkg in enumerate(cache.packages):
    if 1:
        ads2 = {}
        special = ['strawlab.org','ros.org']
        any_special=False
        for version in pkg.version_list:

            site = None
            for pfile, _ in version.file_list:
                if pfile.index_type=='Debian Package Index':
                    site = pfile.site
                    break # do not care about multiple mirrors
            if site is None:
                continue # no file available for this version
            ads2[version.ver_str] = site
            for special_site in special:
                if site.endswith(special_site):
                    any_special=True
        if any_special and len(ads2) >= 2:
            ads1[pkg.name] = ads2
print(json.dumps(ads1,sort_keys=True,
                 indent=4))
