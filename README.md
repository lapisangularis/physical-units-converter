# Physical Units Converter
5 minute test project by lapisangularis

## Installation 
#### Requirements
Application works fine on the newest Windows, MacOSX and linux distributions.

#### Installation & Running
Double click on the executable.

## Usage
Write your value in the first field. Pick your conversion method from available buttons. Click the reset button for the default value and conversion (1kg to lb). Converted value will appear in the second field.
## Development

#### Requirements 

 - `python 3.7.3`
 - `pip 20.1.1`
 
#### Setting up project

If you meet the `Requirements`, you can develop this codebase, just need to setup the environment.

Instructions to do in commandline or terminal:

 1. Go to main folder of the project
  - Windows `cd c:\path\to\project`
  - MacOSX and Linux `cd /path/to/project`
 2. Create new virtualenv
  - `python3 -m venv venv`
 3. Activate virtualenv
  - Windows `call venv/scripts/activate.bat`
  - MacOSX and Linux `source venv/bin/activate`
 4. Install packages with `pip`
  - `pip install -r requirements.txt `

For running the app, type:
 - `fbs run`

#### Executable, compilation

For creating executable, after `Setting up project` part, you just need to type.

 - `fbs freeze`
 
In project folder there will be `target` folder with executable inside. (`.exe` for Windows, `.app` for MacOSX, binary for Linux)
