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
    titulo: '[Nome da Clínica] — Odontologia em [City]',
    descricao: '[Descrição curta da clínica para buscadores, até ~155 caracteres.]',
  },

  marca: {
    nome: '[Nome da Clínica]',
    nomeCurto: '[nome]',
    descritor: 'Dentistry',
    cores: { primaria: '#5B1626' }, // contraste com texto claro ≥ 4,5:1 (o build avisa)
  },

  contato: {
    whatsapp: '[55DDD000000000]', // só dígitos, com DDI 55
    telefone: '[(00) 0000-0000]',
    email: '[hello@example-dental.com]',
    redes: {},
  },

  hero: {
    local: 'Modern dentistry · [Neighborhood, City]',
    titulo: 'Thoughtful care for\nyour *best smile.*',
    texto: '[Frase de apresentação da clínica.]',
    visual: '3d',
  },

  tratamentos: [
    {
      slug: 'avaliacao',
      nome: 'Avaliação',
      resumo: '[Uma frase sobre a avaliação.]',
      descricao: ['[Texto próprio sobre a avaliação, revisado pelo responsável técnico.]'],
    },
  ],

  especialidades: [],

  unidades: [
    {
      id: 'principal',
      nome: '[Nome da unidade]',
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]' },
      horarios: [{ dias: 'Mon–Fri', horas: '[8h–18h]' }],
      fotos: [],
    },
  ],

  agendamento: {
    titulo: 'Ready for a *healthier smile?*',
    texto: 'Choose your preferred time of day. Our team will confirm the appointment with you on WhatsApp.',
    motivos: ['New patient consultation', 'Other'],
  },

  legal: {
    responsavelTecnico: { nome: 'Dr. [Full Name]', cro: '[CRO-UF 00000]' },
    razaoSocial: '[Registered business name]',
    cnpj: '[Business registration number]',
    encarregado: { email: '[privacy@example-dental.com]' },
  },
});
