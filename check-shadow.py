from __future__ import print_function
import apt_pkg
import json
import sys

# init the package system
apt_pkg.init()
cache = apt_pkg.Cache()

def get_packages_with_multiple_versions_from_sites(sites):
    '''return names of packages that are available in multiple versions with at least one such version available at a site specified

    arguments
    ---------
    sites - a list of strings (e.g. ["ros.org","strawlab.org"])

    returns
    -------
    packages_dict

    where packages_dict is in the following form:
    {"package_name":{"version_string1":"site1",
                     "version_string2":"site2"}}
    '''
    packages_dict = {}
    for i,pkg in enumerate(cache.packages):
        if 1:
            package_dict = {}
            any_special=False
            for version in pkg.version_list:

                site = None
                for pfile, _ in version.file_list:
                    if pfile.index_type=='Debian Package Index':
                        site = pfile.site
                        break # do not care about multiple mirrors
                if site is None:
                    continue # no file available for this version
                package_dict[version.ver_str] = site
                for special_site in sites:
                    if site.endswith(special_site):
                        any_special=True
            if any_special and len(package_dict) >= 2:
                packages_dict[pkg.name] = package_dict
    return packages_dict

def cli_print_all():
    sites = sys.argv[1:]
    assert len(sites)>=1
    ads1 = get_packages_with_multiple_versions_from_sites(sites)
    print(json.dumps(ads1,sort_keys=True,
                     indent=4))

if __name__=='__main__':
    cli_print_all()
