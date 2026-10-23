/**
 * Textos anatômicos neutros usados na cena de tratamentos (legendas do
 * quadro B e abas do mobile). Eles apenas NOMEIAM estruturas — não indicam
 * tratamentos nem sugerem diagnóstico. Fazem parte do template, não do cliente.
 */
export const CAMADAS = [
  {
    id: 'esmalte',
    nome: 'Enamel',
    texto: 'The hardest substance in the body, enamel protects the outer surface of a tooth.',
  },
  {
    id: 'dentina-polpa',
    nome: 'Dentin and pulp',
    texto: 'Dentin supports enamel and protects the pulp, which contains nerves and blood vessels.',
  },
  {
    id: 'raiz',
    nome: 'Root',
    texto: 'Below the gumline, the root anchors the tooth to the jawbone.',
  },
] as const;

/** Legendas do quadro B, de cima para baixo (âncoras 3D em scripts/three/anchors.ts). */
export const LEGENDAS = [
  { id: 'esmalte', nome: 'Enamel', texto: 'The outer layer and the hardest substance in the body.' },
  { id: 'polpa', nome: 'Pulp', texto: 'Nerves and blood vessels that nourish the tooth.' },
  { id: 'dentina', nome: 'Dentin', texto: 'Supports enamel and protects the pulp.' },
  { id: 'raiz', nome: 'Root', texto: 'Anchors the tooth to the jawbone.' },
] as const;
