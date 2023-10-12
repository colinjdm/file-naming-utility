# File Naming Utility
#### Video Demo:  https://youtu.be/ha25M3DEXXs
#### Description:

The File Naming Utility is designed to speed up the process of naming files for the public record.  These files can include letters, reports, emails, memos, and other documents.  These documents are all part of the public record and must be available to the public when requested.  Documents are associated with specific "facilities" or "sites" throughout the state.

File names for these documents include a great deal of data.  A typical file name consists of:
```
Master ID
Permit Number
County Code
Document Date
Document Type
Initials
Document Title
```
As document counts increase, manually entering this amount of data into a "Save As" dialogue box in Word or Adobe PDF can take a significant amount of time and incur a great deal of errors.  The File Naming Utility is designed to eliminate those errors by providing data for each site and copying it to the clipboard with one click.

The File Naming Utility is written in Python and incorporates the Flask framework.  Additionally, SQL, HTML, and Javascript are used.

#### Homepage

The homepage allows users to manually enter all data associated with the intended file name.  Three of these categories will not change with each document: Master ID, Permit Number, and County Code.  Once these are entered, they will remain on the page until changed or removed.  The following fields will be changed as necessary for each document.

As data is entered, the file name appears below.  Whenever the file name is complete and the user is satisfied, the user can click the "copy" button to automatically copy the file name to the clipboard.  The file name can now be pasted into the appropriate Word or Adobe PDF dialogue box.

Floating tooltips that give additional instructions for each field are provided by mousing over the field headers.  These tooltips were implemented in Java and move with the mouse.

#### Facilities

This page shows all the data that is available for every facility that is currently in the SQL database.  The user can scroll to locate the appropriate site that they wish to enter documents for.  When the user clicks the "Enter Documents" button, the available data is imported directly into the File Naming Utility on the homepage.

Additionally, users can search for a particular site by name via the search box at the top of the page.  Partial names will work.

#### County Codes

County codes for the document name correspond to the FIPS county codes.  This page allows the user to look up the appropriate county code for sites in Alabama.  This data is read from the "static/ALcounties.csv" file.

# Files

#### app.py
This file uses a Flask framework.  CSV, SQL, and Flask libraries are imported.  The "filenaming.db" SQL file is initialized.

**@app.route("/")** renders "index.HTML" if using the GET method, and "indexed.html" if using the POST method.  If using POST, the variables from the Facilities page are passed into the render_template, in order to be able to autocomplete the available fields.  If a field is not available, app.py saves the variable as a blank space, rather than "None", which is imported from the HTML language.

**@app.route("/sites")** also uses both the GET and POST methods.  If using GET, the file queries the SQL file for all facilities in the database and orders them by name.  These facilities are returned to sites.html.  If using POST, the file imports the search term from sites.html and queries the SQL database using that term.  These facilities are returned to sites.html

**@app.route("/counties")** is a static page that reads the CSV file "ALcounties.csv" and places the data in a table.  The file also strips any blankd space from the county names.  These data are saved as a list of dictionaries, and are passed into counties.html

#### filenaming.db

This is the SQL file associated with the application.  Data were imported from an excel file.  The database entries contain fields for masterid, name, permit number, county, and a unique numeric identifier.

#### tabledata.csv

This is the raw data that was imported into the SQL database.

#### tableinsert.py

This file was created solely to import data from tabledata.csv into the SQL database.  It is written in Python.  It initializes the database, reads the CSV using csv.reader(), and then iterates through every row of the CSV, saving the data into a dictionary of names and masterids.  Unfortunately, permit numbers and county codes were not available as part of this CSV, so those values are being manually entered over time.  This file has only been run once, as running it additionally would create duplicate entries in the SQL database.  Therefore, it should not be run again, and the "db.execute" line has been commented out as a safety precaution.

#### requirement.txt

This file is a flask requirement.

#### static/ALcounties.csv

This is the raw CSV data for Alabama counties used in counties.html

#### static/styles.css

This is the CSS stylesheet.  Many default Bootstrap values were used in the application, but this CSS sheet changes some key colors, including the title and the background.  The #tooltip provides some requirements for the Javascript tooltips that are present on the homepage.

#### statics/js/tooltip.js

This Javascript function is called by index.html and indexed.html.  It provides a floating tooltip to the user whenever the user mouses over one of the headers, providing additional information.  The first seven sections of the function are used to associate the specific tooltip with each header.  The tooltip text is modified using "innerText".  The specific tooltip is identified by ID using getElementById.

The next section of the tooltip watches for the mouseover of each header and executes a function.  It uses tooltip.style.display = 'block' to make the text visible.  It also uses event.clientX and event.clientY to offset the tooltip from the mouse by 10px each.

The final section of the tooltip executes onmouseout.  It hides the tooltip by exectuing tooltip.style.display = 'none'.

#### templates/layout.html

This html page provides the layout for every page in the application.  It uses Jinja syntax to provide room to expand a title block, navbar block, and main block into every page of the site.  Layout.html also uses the meta tags to provide some responsiveness, and initializes both the Bootstrap CSS and local CSS pages.

#### templates/index.html

This page includes the main utility of the application.  It allows the user to enter information for each category in the intended file name.  This data is concatenated live using Javascript.  The HTML itself is laid out in a table.  Each column has a header with an input field below it.  A script element watches for inputs using querySelectorAll for the class ".input".  Each of these inputs is concatenated and saved into a single variable, which is displayed below the table.

A copy button is provided adjacent to the resulting filename, which allows the user to copy the filename to the clipboard with just one click.  This is executed by another short javascript function.

A final Javascript function, tooltip(), is called by mousing over each of the column headers.  This was a design choice and wasn't entirely necessary for the functionality of the application.  But this allows for a cleaner look while also allowing me to supply any helpful information that the user may need if they are unfamiliar with the filing system.

#### /templates/counties.html

This page displays the FIPS county code for every county in Alabama.  This information is important to the filing process, and yet is sometimes difficult to locate.  The HTML file uses a similar table to index.html, while also incorporating a loop.  Jinja syntax is used to loop through the list of dictionaries that is passed to the page.  A "table-hover" class is implemented via bootstrap to make the table more readable.

#### /templates/sites.html

This page incorporates a similar table and Jinja loop to counties.html, but this page is receiving entries from the SQL database, rather than a CSV file.  The list of dictionaries is looped through, and the dictionary values are both displayed as the table data and saved as the HTML value for each input field.

A submit button is added as the last column of each row.  Clicking this submit button sends the available HTML values back to indexed.html via POST.  This auto-fills any of the available data into the file naming utility, preventing the user having to manually copy data from the table of facilities.

A search button is also provided on this page.  This button executes a SQL command that filters the SQL entries by facility name.  Partial names will provide a list of matching facility names.

#### /templates/indexed.html

This final HTML page is almost identical to the homepage index.html.  However, this page utilizes the POST method to auto-fill any data that the user wants to carry over from sites.html.  The first three columns in the table a given a HTML value that is equal to the values provided from sites.html.  However, if the user wishes to change these values, perhaps after moving on to another facility, they can simply overwrite these values.

# Final Thoughts

A few design choices were made regarding this application.  For one, I tried to avoid any obstacle to actually doing work with the application.  That meant that I avoided requiring the user to create a profile and sign in, or being forced to pre-enter any data.  Many users with know some of this information by heart, and will simply want to enter data manually.

Second, I wanted to make sure the SQL database was preserved.  I contemplated allowing the user to add their own facilities to the database, but this would require some degree of QC oversight and time commitment that isn't feasible.  A change could be implemented in the future to allow users to implement new facilities only for their session, but this would again require logins and profiles.

Finally, I wanted to make it somewhat clear that this site is unofficial, hence the lack of branding.  This application is simply an in-house tool, designed to save time on a somewhat tedious task.