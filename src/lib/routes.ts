/**
 * Rotas públicas derivadas da configuração. Usadas por getStaticPaths,
 * pelo sitemap e pelos testes — uma seção desligada não gera página nem link.
 */
import site from './site';

export function rotaEquipeAtiva(): boolean {
  return site.ativo('equipe');
}

export function rotaUnidadesAtiva(): boolean {
  return site.ativo('unidades') && site.multiUnidade;
}

export function rotaSobreAtiva(): boolean {
  return site.ativo('sobre');
}

export function rotasPublicas(): string[] {
  const c = site.c;
  const r = ['/', '/treatments/', ...c.tratamentos.map((t) => `/treatments/${t.slug}/`), '/contact/', '/privacy/'];
  if (rotaSobreAtiva()) r.push('/about/');
  if (rotaEquipeAtiva()) r.push('/team/', ...site.equipeComPagina.map((p) => `/team/${p.slug}/`));
  if (rotaUnidadesAtiva()) r.push('/locations/', ...c.unidades.map((u) => `/locations/${u.id}/`));
  return r;
}
