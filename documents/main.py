"""
MkDocs Macros for Tournament Organizer Documentation

This module provides custom macros for dynamic content generation,
including last updated information and other useful utilities.
Also includes hooks for social media meta tags.
"""

import datetime
import subprocess
from pathlib import Path


def define_env(env):
    """
    Define custom macros for MkDocs
    """

    @env.macro
    def last_updated(page_path=None):
        """
        Get the last updated date for a page using git or file modification time
        Falls back gracefully if git is not available
        """
        try:
            # Try to get git last modified date for the current page
            if page_path:
                # Get the actual file path relative to docs directory
                docs_dir = Path(env.conf["docs_dir"])
                file_path = docs_dir / page_path

                if file_path.exists():
                    # Try git first
                    try:
                        result = subprocess.run(
                            ["git", "log", "-1", "--format=%cd", "--date=format:%B %d, %Y", str(file_path)],
                            capture_output=True,
                            text=True,
                            cwd=docs_dir.parent,
                            check=False,  # Go to documents directory where .git is
                        )
                        if result.returncode == 0 and result.stdout.strip():
                            return result.stdout.strip()
                    except Exception:
                        pass

                    # Fallback to file modification time
                    mtime = file_path.stat().st_mtime
                    return datetime.datetime.fromtimestamp(mtime).strftime("%B %d, %Y")

            # Ultimate fallback - current date
            return datetime.datetime.now().strftime("%B %d, %Y")

        except Exception:
            # If everything fails, return current date
            return datetime.datetime.now().strftime("%B %d, %Y")

    @env.macro
    def build_date():
        """Get the current build date"""
        return datetime.datetime.now().strftime("%B %d, %Y")

    @env.macro
    def git_info():
        """Get git repository information"""
        try:
            # Get current commit hash
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                capture_output=True,
                text=True,
                cwd=Path(env.conf["docs_dir"]).parent,
                check=False,
            )
            if result.returncode == 0:
                commit_hash = result.stdout.strip()
                return f"Commit: {commit_hash}"
        except Exception:
            pass
        return "Git info unavailable"

    @env.macro
    def page_info():
        """
        Generate a complete page info block with last updated date
        """
        # Get page path from environment variables
        page_path = None
        if hasattr(env, "variables") and env.variables:
            # Try different ways to get the page path
            page_path = (
                env.variables.get("page.file.src_path")
                or env.variables.get("page.file.src_uri")
                or env.variables.get("page.file.name")
                or "index.md"
            )
        else:
            page_path = "index.md"

        updated = last_updated(page_path)
        build = build_date()

        return f"""
!!! info "Page Information"
    **Last Updated:** {updated}
    **Build Date:** {build}
    **Page:** `{page_path}`
"""

    @env.macro
    def simple_last_updated():
        """
        Simple last updated macro for inline use
        """
        page_path = env.variables.get("page.file.src_path", "")
        return last_updated(page_path)

    @env.macro
    def footer_info():
        """
        Generate a simple footer with last updated info
        """
        page_path = env.variables.get("page.file.src_path", "")
        updated = last_updated(page_path)
        return f"*Last updated: {updated}*"

    @env.macro
    def social_meta_tags(title=None, description=None, image=None, url=None):
        """
        Generate social media meta tags for Open Graph and Twitter Cards
        """
        # Default values
        site_name = "Tournament Organizer Documentation"
        default_title = "Tournament Organizer Docs"
        default_description = "Comprehensive documentation for the Tournament Organizer project including domains, architecture, and development guides"
        default_image = "https://wpjwegman.github.io/TO-Documentation/assets/images/social-preview.png"
        base_url = "https://wpjwegman.github.io/TO-Documentation"

        # Use provided values or defaults
        meta_title = title or default_title
        meta_description = description or default_description
        meta_image = image or default_image
        meta_url = url or base_url

        # Current page path for URL generation
        if hasattr(env, "variables") and env.variables:
            page_path = env.variables.get("page.file.src_path", "index.md")
            if page_path != "index.md":
                # Convert path to URL format
                page_url = page_path.replace(".md", "/").replace("\\", "/")
                meta_url = f"{base_url}/{page_url}"

        # Generate meta tags HTML
        meta_tags = f"""
<!-- Open Graph Meta Tags -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="{site_name}">
<meta property="og:title" content="{meta_title}">
<meta property="og:description" content="{meta_description}">
<meta property="og:image" content="{meta_image}">
<meta property="og:url" content="{meta_url}">

<!-- Twitter Cards Meta Tags -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{meta_title}">
<meta name="twitter:description" content="{meta_description}">
<meta name="twitter:image" content="{meta_image}">

<!-- Additional SEO Meta Tags -->
<meta name="description" content="{meta_description}">
<link rel="canonical" href="{meta_url}">
"""
        return meta_tags

    @env.macro
    def header_info():
        """
        Generate a header with last updated info for important pages
        """
        page_path = env.variables.get("page.file.src_path", "")
        updated = last_updated(page_path)
        return f"""
!!! note "Documentation Status"
    📅 **Last Updated:** {updated}
"""


def on_page_markdown(markdown, page, config, files):
    """
    Hook to process page content before conversion to HTML
    """
    return markdown


def on_page_content(html, page, config, files):
    """
    Hook to process page content after conversion to HTML
    """
    return html


def on_post_page_macros(env):
    """
    Hook to modify the final HTML output to add social media meta tags
    This is called by the macros plugin after page processing
    """
    # This function is called with the macros environment
    # The actual HTML manipulation needs to be done differently


def on_post_build(env):
    """
    Hook called after the build is complete
    This allows us to modify generated HTML files
    """
    from pathlib import Path

    config = env.conf
    site_dir = Path(config["site_dir"])

    # Define social media meta tags template
    site_name = config.get("site_name", "Tournament Organizer Documentation")
    site_description = config.get(
        "site_description",
        "Comprehensive documentation for the Tournament Organizer project including domains, architecture, and development guides",
    )
    site_url = config.get("site_url", "https://wpjwegman.github.io/TO-Documentation")
    site_author = config.get("site_author", "wpjwegman")

    # Process all HTML files in the site directory
    for html_file in site_dir.rglob("*.html"):
        try:
            with open(html_file, encoding="utf-8") as f:
                content = f.read()

            # Extract page title from the HTML
            title_start = content.find("<title>")
            title_end = content.find("</title>")
            if title_start != -1 and title_end != -1:
                page_title = content[title_start + 7 : title_end]
            else:
                page_title = site_name

            # Get relative URL for this page
            rel_path = html_file.relative_to(site_dir)
            if rel_path.name == "index.html":
                page_url = f"{site_url.rstrip('/')}"
                if rel_path.parent != Path():
                    page_url += f"/{rel_path.parent.as_posix()}"
            else:
                page_url = f"{site_url.rstrip('/')}/{rel_path.with_suffix('').as_posix()}"

            # Social image placeholder
            social_image = f"{site_url.rstrip('/')}/assets/images/social-preview.png"

            # Create meta tags
            social_meta_tags = f"""
  <!-- Open Graph Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{site_name}">
  <meta property="og:title" content="{page_title}">
  <meta property="og:description" content="{site_description}">
  <meta property="og:image" content="{social_image}">
  <meta property="og:url" content="{page_url}">

  <!-- Twitter Cards Meta Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page_title}">
  <meta name="twitter:description" content="{site_description}">
  <meta name="twitter:image" content="{social_image}">

  <!-- Additional SEO Meta Tags -->
  <meta name="author" content="{site_author}">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{page_url}">"""

            # Insert meta tags before </head>
            if "</head>" in content:
                content = content.replace("</head>", social_meta_tags + "\n  </head>")

                # Write the modified content back
                with open(html_file, "w", encoding="utf-8") as f:
                    f.write(content)

        except Exception as e:
            print(f"Warning: Could not process {html_file}: {e}")
            continue
