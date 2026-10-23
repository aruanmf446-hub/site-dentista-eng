/**
 * MODELO PARA UMA NOVA CLÍNICA
 *
 * Não edite este arquivo diretamente. Crie o cliente com:
 *   node scripts/nova-clinica.mjs nome-da-clinica
 * e edite src/clients/nome-da-clinica/clinic.ts.
 *
 * Regras (ver CUSTOMIZATION.md e COMPLIANCE.md):
 * - Tudo entre [colchetes] é placeholder. Substitua por dados REAIS e
 *   verificados. Com `site.modo: 'producao'` o build falha se sobrar algum.
 * - Nunca invente profissionais, CRO, endereços, convênios, preços ou avaliações.
 * - Fotos: coloque os arquivos em ./fotos/ e importe (import fachada from './fotos/fachada.jpg').
 * - Textos de tratamento são conteúdo da clínica: escreva e revise com o
 *   responsável técnico.
 */
import { defineClinic } from '../../config/clinic.schema';
// import fachada from './fotos/fachada.jpg';

export default defineClinic({
  site: {
    modo: 'demonstracao', // troque para 'producao' quando os dados estiverem completos
    url: 'https://www.your-dental-practice.com', // troque pelo domínio real
    titulo: '[Practice Name] — Dental Care in [City]',
    descricao: '[Brief, accurate practice description for search engines.]',
  },

  marca: {
    nome: '[Practice Name]',
    nomeCurto: '[brand]',
    descritor: 'Dentistry',
    cores: { primaria: '#5B1626' }, // contraste com texto claro ≥ 4,5:1 (o build avisa)
  },

  contato: {
    whatsapp: '[International WhatsApp number]', // só dígitos, com DDI 55
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
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]' },
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
