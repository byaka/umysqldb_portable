import platform, sys
vers=sys.version[:3]
arch=platform.architecture()[0]

if vers=='2.7' and arch=='64bit':
    from py27x64 import umysql
elif vers=='2.6' and arch=='32bit':
    from py26x32 import umysql
else:
    raise ImportError('Unsupported platform: %s %s'%(vers, arch))

__all__=['umysql']
