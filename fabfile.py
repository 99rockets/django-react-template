from fabric.api import local


def webpack():
    """
    Clears the /assets/bundles folders and re-creates the bundles.
    This should be run every time we made changes to ReactJS before we commit
    and push our code.
    """
    local('rm -rf assets/bundles/local/*')
    local('rm -rf assets/bundles/prod/*')
    local('webpack --config webpack.local.config.js --progress --colors')
    local('webpack --config webpack.prod.config.js --progress --colors')
