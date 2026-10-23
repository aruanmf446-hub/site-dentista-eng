/**
 * CLIENTE DE DEMONSTRAÇÃO — Alva Dental (identidade fictícia do Claude Design).
 *
 * Tudo entre [colchetes] é placeholder: dado que a clínica real precisa
 * fornecer. Nada aqui representa profissionais, endereços, convênios,
 * preços ou avaliações reais. Os textos educativos sobre tratamentos são
 * exemplos e precisam ser revisados pelo responsável técnico de cada cliente.
 */
import { defineClinic } from '../../config/clinic.schema';

export default defineClinic({
  site: {
    modo: 'demonstracao',
    url: 'https://example-dental-practice.com',
    titulo: 'Alva Dental — website demo',
    descricao:
      'Modern dental care with comprehensive assessments, clear treatment plans and supportive follow-up.',
  },

  marca: {
    nome: 'Alva Dental',
    nomeCurto: 'alva',
    descritor: 'Dentistry',
    cores: { primaria: '#5B1626' },
  },

  contato: {
    // Sem número central: com várias unidades, o visitante escolhe a unidade antes do WhatsApp.
    telefone: '[+1 (000) 000-0000]',
    email: '[hello@example-dental.com]',
    redes: { instagram: 'https://www.instagram.com/' },
  },

  hero: {
    local: 'Modern dentistry · [Neighborhood, City]',
    titulo: 'Thoughtful care for\nyour *best smile.*',
    texto:
      'Comprehensive consultations, personalized treatment plans and a welcoming team by your side at every step.',
    visual: '3d',
    nota: 'Mon–Fri [8 am–8 pm] · Sat [8 am–1 pm] · [Insurance and self-pay patients welcome]',
  },

  tratamentos: [
    {
      slug: 'checkups-and-prevention',
      nome: 'Dental checkups & prevention',
      resumo: 'A complete dental checkup to understand your oral health and plan next steps.',
      descricao: [
        'A dental examination is the starting point for any treatment. Your dentist assesses your teeth, gums, bite and oral tissues, and discusses your concerns, habits and medical history.',
        'If needed, the dentist may recommend imaging. You will receive a clearly explained treatment plan with priorities and available options.',
      ],
      etapas: [
        { titulo: 'Initial conversation', texto: 'Medical history, concerns and expectations.' },
        { titulo: 'Clinical examination', texto: 'Teeth, gums, bite and soft tissues.' },
        { titulo: 'Treatment plan', texto: 'Priorities, options and next steps.' },
      ],
    },
    {
      slug: 'teeth-cleaning',
      nome: 'Teeth cleaning',
      resumo: 'Professional plaque and tartar removal, plus tailored oral hygiene guidance.',
      descricao: [
        'Professional cleaning removes plaque and tartar that brushing alone cannot remove, particularly along the gumline and between the teeth.',
        'Your dental team can also review brushing and flossing techniques. Your dentist will recommend a cleaning schedule suited to your needs.',
      ],
      camadas: ['esmalte'],
    },
    {
      slug: 'teeth-whitening',
      nome: 'Teeth whitening',
      resumo: 'Professional teeth whitening supervised by a dentist following an examination.',
      descricao: [
        'Teeth whitening uses specially formulated gels to lighten tooth color. Before treatment, your dentist checks for decay, sensitivity and existing restorations.',
        'In-office, professionally supervised at-home or combined options may be recommended. Fillings and crowns do not whiten and may require adjustment afterward.',
      ],
      camadas: ['esmalte'],
    },
    {
      slug: 'dental-fillings',
      nome: 'Fillings',
      resumo: 'Restore the shape and function of teeth affected by cavities or damage.',
      descricao: [
        'A filling replaces damaged tooth structure with a tooth-colored material to restore shape and chewing function.',
        'For extensive damage, your dentist may recommend a custom inlay or onlay made outside the mouth and bonded in place.',
      ],
      camadas: ['esmalte', 'dentina-polpa'],
    },
    {
      slug: 'dental-veneers',
      nome: 'Dental veneers',
      resumo: 'Thin custom shells that improve the color, shape or appearance of front teeth.',
      descricao: [
        'Veneers are thin porcelain or composite shells applied to the visible surface of teeth to improve color, shape and small gaps.',
        'Planning includes an assessment of your bite and gums and may include a preview of the expected result.',
      ],
      camadas: ['esmalte'],
      especialidade: 'estetica-e-protese',
    },
    {
      slug: 'root-canal-treatment',
      nome: 'Root canal treatment',
      resumo: 'Treat the dental pulp to relieve discomfort and help preserve your natural tooth.',
      descricao: [
        'When the tooth pulp becomes inflamed or infected, root canal treatment cleans, disinfects and seals the inner canals.',
        'The goal is to save your natural tooth. A filling or crown may be needed afterward to protect it.',
      ],
      camadas: ['dentina-polpa'],
      especialidade: 'endodontia',
    },
    {
      slug: 'dental-implants',
      nome: 'Dental implants',
      resumo: 'Replace missing teeth with implants, from planning through long-term care.',
      descricao: [
        'A dental implant is a small post, usually made of titanium, placed in the jawbone to replace a missing tooth root and support a crown or other restoration.',
        'Planning considers jawbone volume, gum health and your overall health. Treatment stages and timelines vary by patient.',
      ],
      camadas: ['raiz'],
      especialidade: 'implantodontia',
      exibirNaHome: false,
    },
    {
      slug: 'crowns-and-dentures',
      nome: 'Prosthetics',
      resumo: 'Crowns, bridges and dentures to restore damaged or missing teeth.',
      descricao: [
        'Dental prosthetics replace missing teeth or rebuild heavily worn teeth. Options include crowns, bridges, removable dentures and implant-supported restorations.',
        'Your options depend on the teeth involved, gum and bone health, and your personal preferences.',
      ],
      especialidade: 'estetica-e-protese',
      exibirNaHome: false,
    },
    {
      slug: 'braces-and-aligners',
      nome: 'Braces & clear aligners',
      resumo: 'Improve alignment and bite using braces or clear aligners.',
      descricao: [
        'Orthodontic treatment aligns teeth and corrects bite issues using braces or removable clear aligners.',
        'For children and teenagers, an orthodontist also monitors facial growth to determine when treatment may be most helpful.',
      ],
      especialidade: 'ortodontia',
      exibirNaHome: false,
    },
    {
      slug: 'gum-disease-treatment',
      nome: 'Gum disease treatment',
      resumo: 'Prevent and manage gum inflammation and bleeding.',
      descricao: [
        'Bleeding, swelling and receding gums may indicate periodontal disease. Care may include deep cleaning below the gumline and regular follow-up.',
        'Healthy gums help protect the bone supporting your teeth and are essential to many other dental treatments.',
      ],
      camadas: ['raiz'],
      especialidade: 'periodontia',
      exibirNaHome: false,
    },
  ],

  especialidades: [
    {
      slug: 'ortodontia',
      nome: 'Orthodontics',
      descricao: 'Braces, clear aligners and orthodontic growth monitoring.',
      profissionais: ['dentista-ortodontia'],
      destaque: { dentes: 'todos', efeito: 'aparelho' },
    },
    {
      slug: 'implantodontia',
      nome: 'Dental implants',
      descricao: 'Replace missing teeth with implants, from planning through long-term care.',
      profissionais: ['dentista-implantodontia'],
      destaque: { dentes: [1, 12], efeito: 'implante' },
    },
    {
      slug: 'endodontia',
      nome: 'Endodontics',
      descricao: 'Root canal therapy to ease discomfort and preserve natural teeth.',
      profissionais: ['dentista-endodontia'],
      destaque: { dentes: [3], efeito: 'nenhum' },
    },
    {
      slug: 'periodontia',
      nome: 'Periodontics',
      descricao: 'Gum health, preventive care and treatment for inflammation and bleeding.',
      destaque: { dentes: 'todos', efeito: 'gengiva' },
    },
    {
      slug: 'odontopediatria',
      nome: 'Pediatric dentistry',
      descricao: 'Gentle dental care for infants, children and teenagers.',
      profissionais: ['dentista-odontopediatria'],
      destaque: { dentes: 'incisivos', efeito: 'nenhum' },
    },
    {
      slug: 'estetica-e-protese',
      nome: 'Cosmetic & restorative dentistry',
      descricao: 'Veneers, teeth whitening and smile restoration.',
      destaque: { dentes: 'anteriores', efeito: 'nenhum' },
    },
  ],

  sobre: {
    titulo: 'A welcoming space designed *around you.*',
    texto: [
      '[Tell your practice’s story and what makes the patient experience special.]',
    ],
    diferenciais: [
      { texto: '[Documented instrument sterilization procedures]', rotulo: 'Patient safety' },
      { texto: '[Wheelchair accessible]', rotulo: 'Accessibility' },
      { texto: '[Convenient parking]', rotulo: 'Convenience' },
    ],
    fotos: [
      { src: '[Real photo — reception]', alt: 'Practice reception', legenda: 'Reception · Downtown practice' },
      { src: '[Real photo — treatment room]', alt: 'Treatment room', legenda: 'Treatment room' },
    ],
  },

  equipe: [
    {
      slug: 'dentista-ortodontia',
      nome: 'Dr. [Full Name]',
      cro: '[Professional license number]',
      especialidade: 'Orthodontics',
      unidades: ['centro'],
      bio: ['[Short clinician-approved bio: education, areas of expertise and approach to patient care.]'],
      formacao: ['[Degree — University, year]', '[Specialty training — Institution, year]'],
      pagina: true,
    },
    {
      slug: 'dentista-implantodontia',
      nome: 'Dr. [Full Name]',
      cro: '[Professional license number]',
      especialidade: 'Dental implants',
      unidades: ['centro', 'jardins'],
      bio: ['[Short biography approved by the clinician.]'],
    },
    {
      slug: 'dentista-odontopediatria',
      nome: 'Dr. [Full Name]',
      cro: '[Professional license number]',
      especialidade: 'Pediatric dentistry',
      unidades: ['jardins'],
    },
    {
      slug: 'dentista-endodontia',
      nome: 'Dr. [Full Name]',
      cro: '[Professional license number]',
      especialidade: 'Endodontics',
      unidades: ['unidade-3'],
    },
  ],

  unidades: [
    {
      id: 'centro',
      nome: 'Downtown practice',
      nomeCurto: 'Downtown',
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]' },
      horarios: [
        { dias: 'Mon–Fri', horas: '[8 am–8 pm]' },
        { dias: 'Sat', horas: '[8 am–1 pm]' },
      ],
      whatsapp: '[Downtown WhatsApp number]',
      fotos: [{ src: '[Real photo — exterior]', alt: 'Fachada da Downtown practice' }],
    },
    {
      id: 'jardins',
      nome: 'Garden practice',
      nomeCurto: 'Garden',
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]' },
      horarios: [{ dias: 'Mon–Fri', horas: '[8 am–7 pm]' }],
      observacao: '[On-site parking]',
      whatsapp: '[Garden WhatsApp number]',
      fotos: [{ src: '[Real photo — exterior]', alt: 'Fachada da Garden practice' }],
    },
    {
      id: 'unidade-3',
      nome: '[Location 3]',
      nomeCurto: '[Location 3]',
      endereco: { logradouro: '[Street]', numero: '[Number]', bairro: '[Neighborhood]', cidade: '[City]', uf: '[State]' },
      horarios: [{ dias: 'Mon–Fri', horas: '[9 am–6 pm]' }],
      observacao: '[Additional information]',
      whatsapp: '[Location 3 WhatsApp number]',
      fotos: [{ src: '[Real photo — exterior]', alt: 'Fachada da Unidade 3' }],
    },
  ],

  convenios: {
    titulo: 'Accepted insurance plans',
    itens: Array.from({ length: 6 }, (_, i) => ({ nome: `[Insurance logo ${i + 1}]` })),
    observacao: 'Self-pay patients are welcome. [Payment information.]',
  },

  valores: {
    titulo: 'Treatment pricing',
    revisadoPeloResponsavel: false,
    itens: [
      { item: 'Dental consultation', valor: '[Price]' },
      { item: 'Professional cleaning', valor: '[Price]' },
      { item: 'Teeth whitening', valor: 'from [Price]' },
      { item: 'Single dental implant', valor: 'Price on consultation' },
    ],
  },

  depoimentos: [1, 2, 3].map((n) => ({
    texto: `[Excerpt of a genuine patient review published with written permission. Example ${n}.]`,
    autor: '[Patient name]',
    fonte: 'Google review',
    consentimento: false,
  })),

  galeria: {
    titulo: 'Explore our *practice.*',
    fotos: [
      { src: '[Real photo — waiting area]', alt: 'Waiting room', legenda: 'Waiting room' },
      { src: '[Real photo — treatment room]', alt: 'Treatment room', legenda: 'Treatment room' },
      { src: '[Real photo — sterilization area]', alt: 'Sterilization area', legenda: 'Sterilization' },
    ],
  },

  faq: {
    titulo: 'Frequently asked *questions.*',
    itens: [
      {
        pergunta: 'What happens at my first appointment?',
        resposta: '[Describe what happens at the first appointment, how long it takes and what patients should bring.]',
      },
      {
        pergunta: 'Do you accept dental insurance?',
        resposta: '[List accepted insurance plans and how to confirm coverage.]',
      },
      {
        pergunta: 'Do you offer emergency dental care?',
        resposta: '[Explain emergency availability and how to request urgent dental care.]',
      },
    ],
  },

  agendamento: {
    titulo: 'Ready for a *healthier smile?*',
    texto: 'Choose a location and your preferred time of day. Our team will confirm the appointment with you on WhatsApp.',
    motivos: ['New patient consultation', 'Teeth cleaning', 'Tooth pain or emergency', 'Dental implants', 'Orthodontics', 'Other'],
    periodos: ['Morning', 'Afternoon', 'Evening'],
  },

  legal: {
    responsavelTecnico: { nome: 'Dr. [Full Name]', cro: '[Professional license number]' },
    razaoSocial: '[Registered business name]',
    cnpj: '[Business registration number]',
    encarregado: { email: '[privacy@example-dental.com]' },
    politicaAtualizadaEm: '[date]',
  },

  secoes: {
    // Demonstração: todos os módulos visíveis. "valores" vem desligado por padrão
    // no schema; aqui está ligado apenas para exibir o módulo.
    valores: true,
  },
});
