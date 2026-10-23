# Alva Dental — English Website Template

International English-language edition of the [original Portuguese dental website](https://github.com/aruanmf446-hub/site-dentista).

A customizable, responsive Astro website for dental practices with a cinematic 3D tooth animation, treatment pages, clinician profiles, locations, an appointment-request form and SEO metadata.

## Start

Requires Node.js 22.22+ and npm 10+.

    npm ci
    npm run dev
    npm run build
    npm run check

By default the demo uses the fictional Alva Dental practice. **Bracketed details are placeholders, not verified businesses or medical claims.** Replace them before publishing a real client website.

## Customize for a client

    node scripts/nova-clinica.mjs customer-name
    CLINIC=customer-name SITE_URL=https://www.customer-domain.com npm run build

Edit the generated file in `src/clients/customer-name/clinic.ts`. The internal schema names remain Portuguese for compatibility with the original implementation; **visitor-facing copy is English**.

### International launch checklist

- Replace every placeholder with verified clinic, clinician, licensing and contact information.
- Update the practice country, currency, opening hours, phone country codes and payment methods.
- Review the privacy notice and all professional advertising statements under applicable **local** law.
- Configure `SITE_URL` for the real domain and check metadata, canonical URLs and structured data.
- Do not assume an appointment has been booked: the WhatsApp flow only sends an inquiry.
- Confirm the preferred contact method for each market. WhatsApp is available as a starting point, but additional contact integrations may be useful.

## Structure

The template keeps independent configurable sections for treatments, specialties, team, locations, insurance, testimonials, gallery, FAQ and appointment requests. English public routes include `/treatments/`, `/team/`, `/locations/`, `/about/`, `/contact/` and `/privacy/`. The source template remains unchanged.
