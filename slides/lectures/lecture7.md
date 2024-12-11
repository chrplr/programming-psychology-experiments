# Reproducible science

**Aim** Anyone should be able to replicate your experiment, and your analyses.

The Method sections of papers are insufficient.

Solutions:

1. keep a lab notebok (paper or computerized). 

   * Document what you did !!!! 

   * For data analyses, use literate programming (RMarkdown, Python Notebooks, ...)

2. track stuff and use *version control* => Git

   version control hides the past, but keep it accessible.
   It allows you to keep a clean folder.
   
   
 
 
# Hints


* Put a README file inside each folder. 

* keep your git repository small:

- do not put large data files (>10M) inside a git repo. It is for code, documentation, small datasets (e.g. csv). If possible, put data on a public server, e.G. osf, openneuro, ...

- For a given project, you can have several repositories, e.g. one for stimulus creation, one for stimulation, one for data analysys

* You can keep your git repo on your local hardrive, but having a copy of in the cloud, or on backup disks, is a HUGE security.

* have repo in the cloud (e.g. github) allows you to work from several computer, and collaborate.

* Some cloud offer private hosting of git repositories


# How to create a website with github

* Create a git repository on github, clone it locally.

* Populate with some markdown files, images, etc.

* Activate Settings/Pages/Build Deploymentand select the main branch.


After a few minutes, your website will appear at <http://yourlogin.github.io/project_name>



---

 



