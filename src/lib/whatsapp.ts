/**
 * Monta links e mensagens do WhatsApp. Usado no build (links estáticos)
 * e no navegador (formulários). Não envia nada a servidores próprios:
 * o visitante é quem envia a mensagem pelo WhatsApp.
 */
import { PLACEHOLDER_RE } from './placeholders';

export function normalizeNumber(raw: string | undefined | null): string | null {
  if (!raw || PLACEHOLDER_RE.test(raw)) return null;
  const digits = raw.replace(/\D/g, '');
  return digits.length >= 12 ? digits : null;
}

export function waUrl(number: string, text: string): string {
  return `https://wa.me/${number}?text=${encodeURIComponent(text)}`;
}

export interface PedidoContato {
  nome?: string;
  unidade?: string;
  motivo?: string;
  periodo?: string;
  tratamento?: string;
}

/** Mensagem organizada, sem dados sensíveis (não pede CPF, sintomas detalhados etc.). */
export function buildMensagem(p: PedidoContato): string {
  const linhas: string[] = [];
  linhas.push(p.nome ? `Hello! My name is ${p.nome.trim()}.` : 'Hello!');
  linhas.push(
    p.tratamento
      ? `I’d like to learn more and request an appointment for ${p.tratamento}.`
      : 'I’d like to request an appointment.',
  );
  if (p.unidade) linhas.push(`• Location: ${p.unidade}`);
  if (p.motivo) linhas.push(`• Reason for visit: ${p.motivo}`);
  if (p.periodo) linhas.push(`• Preferred time of day: ${p.periodo}`);
  linhas.push('I look forward to arranging a convenient time.');
  return linhas.join('\n');
}
