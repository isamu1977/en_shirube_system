## Context
Generating high-quality PDFs containing complex Japanese typography and layout (Flexbox/Grid) requires a capable rendering engine. Standard Python PDF libraries often struggle with modern CSS and Asian fonts.

## Goals / Non-Goals
- **Goals**:
  - Deliver a beautiful, multi-page PDF reading report that matches the high-end, premium aesthetic of the site.
  - Implement robust HTML-to-PDF conversion supporting `Noto Serif JP` or `Shippori Mincho`.
- **Non-Goals**:
  - Building a full document management system; PDFs are generated per reading and potentially cached/stored in S3 or R2.

## Decisions
- **PDF Engine**: Playwright (Async) is recommended as the primary choice due to its flawless rendering of modern CSS and web fonts, given the "premium, minimalist, and editorial" requirements. Alternatively, WeasyPrint can be explored if Playwright adds too much overhead to the Docker image, but WebKit/Chromium ensures exact fidelity.
- **Template Engine**: Jinja2 will be used to inject reading data into a pre-designed HTML template before rendering it to PDF.
- **Styling**: The CSS will utilize `@page` for A4 portrait sizing, strict margins (20mm), soft dark grey text `#333333`, and a pale beige background `#FAF9F6`.

## Risks / Trade-offs
- **Performance**: Starting a headless browser (Playwright) or running a heavy rendering engine for each PDF request can be resource-intensive.
  - *Mitigation*: Generate the PDF asynchronously upon reading completion and store it (e.g., S3/R2), or efficiently pool browser instances.
- **Docker Size**: Including Chromium/WebKit increases the backend container size significantly.
  - *Mitigation*: Ensure the Dockerfile is optimized, or use WeasyPrint if the CSS requirements can be strictly met without a full browser engine.
