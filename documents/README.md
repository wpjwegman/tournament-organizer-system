# Tournament Organizer Documentation Pipeline

![Documentation Build](https://github.com/wpjwegman/TO-Documentation/actions/workflows/docs.yml/badge.svg)

**⚠️ IMPORTANT: All documentation work is done exclusively in the `/documents` folder!**

This folder contains the **complete MkDocs documentation pipeline** for the Tournament Organizer project.

## 📁 Folder Structure

```
/documents/         # Complete MkDocs documentation pipeline (WORK HERE ONLY)
├── docs/           # ALL source documentation content
├── site/           # Generated static site output
├── mkdocs.yml      # MkDocs configuration
├── README.md       # This file
└── requirements.txt # Python dependencies
```

## 🎯 Purpose

- **`/documents/docs/`** - Contains ALL documentation content (domains, architecture, development guides, etc.)
- **`/documents/site/`** - Generated static website output
- **Legacy `/docs/` folder exists but is NOT used for documentation work**

## 🚀 Local Development

### Start the documentation server:
```bash
cd documents
mkdocs serve
```

### Build the static site:
```bash
cd documents
mkdocs build
```

## 📝 Content Management

**⚠️ WORK EXCLUSIVELY IN `/documents` FOLDER:**

1. **ALL content** lives in `/documents/docs/` (domains, architecture, development guides)
2. **Configuration** is managed in `/documents/mkdocs.yml`
3. **Generated site** outputs to `/documents/site/`
4. **Legacy `/docs/` folder is NOT used** for documentation work

## 🏗️ Workflow

1. **Create/Update** documentation in `/documents/docs/`
2. **Configure** navigation in `/documents/mkdocs.yml` if needed
3. **Test** locally with `mkdocs serve` from `/documents/` folder
4. **Build** final site with `mkdocs build` from `/documents/` folder

## ⚠️ Important Notes

- **Never work in the root `/docs/` folder** - it's legacy and not maintained
- **The `/documents/docs/` folder contains the cleaned, link-fixed, most recent content**
- **All documentation work, updates, and maintenance happens in `/documents/` only**

## Project Management

This repository is linked to the [Tournament Organizer Development](https://github.com/users/wpjwegman/projects/4) project for task tracking and project management.## Documentation

- [Architecture Overview](docs/architecture/overview.md)
- [Development Guide](docs/development/README.md)
- [API Documentation](docs/api/README.md)
- [Domain Documentation](docs/domains/overview.md)

## Architecture

- **Backend**: FastAPI with MongoDB
- **Frontend**: React/Next.js (planned)
- **Database**: MongoDB with Motor async driver
- **Authentication**: JWT with role-based access control
- **Testing**: pytest with comprehensive test coverage

## Current Status

- [x] Classification Domain
- [x] Code of Conduct Domain
- [x] Communication Domain
- [x] Discipline Domain
- [x] Finance Domain
- [x] Identity Domain
- [ ] Additional domains in progress

## Contributing

See [Contributing Guide](docs/development/contributing.md) for development guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.
