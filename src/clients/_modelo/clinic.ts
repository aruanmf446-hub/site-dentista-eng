/**
 * Starter profile for a new international dental practice.
 *
 * Create a client using scripts/nova-clinica.mjs, then edit the generated
 * src/clients/<client>/clinic.ts with real verified business details.
 * Bracketed values are placeholders. Do not publish them as real facts.
 * Confirm clinician credentials, photos, insurance, contact information,
 * privacy terms and advertising compliance for each target market.
 */
import { defineClinic } from '../../config/clinic.schema';
// import fachada from './fotos/fachada.jpg';

export default defineClinic({
  site: {
    modo: 'demonstracao', // Switch to 'producao' only when all details are verified.
    url: 'https://www.your-dental-practice.com', // Replace with the live client domain.
    titulo: '[Practice Name] — Dental Care in [City]',
    descricao: '[Brief, accurate practice description for search engines.]',
  },

  marca: {
    nome: '[Practice Name]',
    nomeCurto: '[brand]',
    descritor: 'Dentistry',
    cores: { primaria: '#5B1626' }, // Verify text contrast before publishing.
  },

  contato: {
    whatsapp: '[International WhatsApp number]', // E.164 country code + national number, digits only.
    telefone: '[+1 000 000 0000]',
    email: '[hello@example-dental.com]',
    redes: {},
  },

  hero: {
    local: 'Modern dentistry · [Neighborhood, City]',
    titulo: 'Thoughtful care for\nyour *best smile.*',
    texto: '[A welcoming introduction to your practice.]',
    visual: '3d',
  },

  tratamentos: [
    {
      slug: 'dental-checkup',
      nome: 'Dental checkup',
      resumo: '[One sentence about the consultation.]',
      descricao: ['[Clinician-reviewed copy about the consultation.]'],
    },
  ],

  especialidades: [],

  unidades: [
    {
      id: 'principal',
      nome: '[Practice Location]',
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]', pais: 'US' },
      horarios: [{ dias: 'Mon–Fri', horas: '[9 am–6 pm]' }],
      fotos: [],
    },
  ],

  agendamento: {
    titulo: 'Ready for a *healthier smile?*',
    texto: 'Choose your preferred time of day. Our team will confirm the appointment with you on WhatsApp.',
    motivos: ['New patient consultation', 'Other'],
  },

  legal: {
    responsavelTecnico: { nome: 'Dr. [Full Name]', cro: '[Professional license number]' },
    razaoSocial: '[Registered business name]',
    cnpj: '[Business registration number]',
    encarregado: { email: '[privacy@example-dental.com]' },
  },
});
