import modulefinder

finder = modulefinder.ModuleFinder()
finder.run_script('cosinewave.py')

moduleslist = {}
for name, mod in finder.modules.iteritems():
    filename = mod.__file__
    if filename is None:
        continue
    if '__' in name:
        continue
    #if "python" in filename.lower():
    #    continue
    moduleslist[name.split(".")[0]] = True
    #print '%s: %s' % (name, filename)
    #print ','.join(mod.globalnames.keys()[:3])

print('Loaded modules:')
for name, dummy in moduleslist.iteritems():
    print(name)

input("Press Enter to continue...")
