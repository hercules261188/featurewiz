# -*- coding: utf-8 -*-
################################################################################
#     featurewiz v0.0.1
#     Python v3.6+
#     Created by Ram Seshadri
#     Licensed under Apache License v2
################################################################################
# Version
from .__version__ import __version__

if __name__ == "__main__":
    version_number = __version__
    print("""Running featurewiz version: %s. Call using:
                 features = featurewiz(dataname, target, corr_limit=0.70,
                                verbose=2)""" %version_number)
else:
    version_number = __version__
    print("""Imported featurewiz version: %s. Call using:
                 features = featurewiz(dataname, target, corr_limit=0.70,
                                verbose=2)""" %version_number)
################################################################################