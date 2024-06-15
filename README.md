# Gnome-KDE-XFCE Look

---
### Resources
[pling.com](pling.com)

---
### Project Structure
GKX  
├── gkx  
│   ├── core  
│   ├── resources  
│   │   ├── config  
│   │   ├── icons  
│   │   ├── img  
│   │   └── ui  
│   ├── windows  
│   └── utils  


---
### Global Structure
![global-structure](gkx/resources/img/gxk.svg) 


---
### Milestones
- [X] Scrapper (get search results, get item preview)
- [X] Scrapper (download)
- [X] Search results handler (organizing, filttering, ...)
- [ ] Settings Core
- [ ] Build GUI
- [ ] Implement errors handling system


### Todo
- [X] return ResultsManger from search instead of pandas.DataFrame
- [X] check if pandas presents filtering functionality
- [X] convert 'last-update' to datetime
- [ ] implement settings !important
- [ ] filter categories (supported only)