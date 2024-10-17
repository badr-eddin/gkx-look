# Gnome-KDE-XFCE Look (Web Scrapping)

### Another uncompleted project

*Note: I am sure that the backend is completed , it could be used as a library. I wanted to build A GUI for it but now I got better projects ideas and kind of busy, so maybe in the future*

it could work for other desktop environments (I really do not know)

**No documentation, just read the damn code**

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

### Milestones

- [x] Scrapper (get search results, get item preview)
- [x] Scrapper (download)
- [x] Search results handler (organizing, filttering, ...)
- [ ] Settings Core
- [ ] Build GUI
- [ ] Implement errors handling system

### Todo

- [x] return ResultsManger from search instead of pandas.DataFrame
- [x] check if pandas presents filtering functionality
- [x] convert 'last-update' to datetime
- [ ] implement settings !important
- [ ] filter categories (supported only)