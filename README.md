# Oxide
Oxide is an interface that allows a programmer to systematically extract information from various binary analysis tools using a common API. Oxide's strength is in applying analysis tools to large collections of data. This means, Oxide excels at finding data insights, comparing tool results, preprocessing data, and more on a large collection of programs.

## How do I use Oxide?
Oxide can be interfaced using the Oxide Shell directly or with the RESTful API.

## Terminologies

### Modules
Modules are script bundles that interface with a binary analysis tool to extract common, systematic information about a program. For example, every binary analysis tool will provide to the user a disassembly of the program. The goal of the module is to extract that information and present it to the plugins (analysis tools) with one simple API call. Features that are specific to a binary analysis tool and is not a commonly shared feature of all binary analysis tools may require loading a custom script to that module. 

### Plugins
Plugins are analysis tools designed to use information extracted from modules. The plugin developer then needs not worry about interfacing directly with the various tools and instead use the Oxide API.

Sometimes, you may want to write a tool-specific plugin that works on a collection of programs. This will require writing a custom script that extracts the information from the tool and then adding it to the output.

### Storage
The storage is a flat-file database of cached module and analysis results. Here you will also find a copy of all of the programs in a pickled format. That is, there is no risk of running any program without significant modifications to the content of the file.
