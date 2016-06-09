# The 'views' directory

All views are automatically imported when they are created. However, you
must name them correctly for this to work.

## VERY IMPORTANT NAMING CONVENTION

All views must end with the name "View.py".

For example, valid names include:

* helloView.py
* loginView.py

However, invalid names include:

* helloview.py
* Viewlogin.py

and so on.

# Additional Information about Views

Every file in this directory should represent a "view." There are two schools
of thought to managing views:

* Each file should implement an entire feature.
* Each file should represent a single page.

For small to medium-sized applications (2-20 pages), it is probably best
to have a single file for a single page. It is easier to keep track of what
code is associated with what page, and so on. For larger applications,
it is likely that more structure is needed, and more significant design
(as well as layout of the codebase) is needed than can be discussed here.

In short, every page should have a .py file associated with it, and a
one, or possibly two, related endpoints ("routes") should be defined
in that file.




# Super Mega Hint
The script "create-page" at the top level of this project is recommended,
as it creates a view and template automatically, names them appropriately,
and uses a standard template to get you started.

For example:

./create-page handleLogin

will create all of the files you need to get working on a new login page.
