#!/usr/bin/env python3
"""Localize the cloned dental website into natural English without altering the PT repository.

Run once in the destination repository: python3 scripts/localize-english.py
The internal configuration keys and 3D scene IDs intentionally remain unchanged.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

ROUTES = {
    "/tratamentos/": "/treatments/",
    "/equipe/": "/team/",
    "/unidades/": "/locations/",
    "/a-clinica/": "/about/",
    "/contato/": "/contact/",
    "/privacidade/": "/privacy/",
}

# Human-edited translations of the site chrome, content, accessibility and form feedback.
PHRASES = {
    "O cuidado que\\nfica no seu *sorriso.*": "Thoughtful care for\\nyour *best smile.*",
    "Cuidado em cada detalhe, *por dentro e por fora.*": "Expert care, *inside and out.*",
    "Conheça o dente *por dentro.*": "Discover what's *inside a tooth.*",
    "Esmalte, dentina, polpa e raiz trabalham juntos. Por isso, todo tratamento começa por uma avaliação completa.": "Enamel, dentin, pulp and roots work together. That's why every treatment starts with a thorough examination.",
    "O que podemos *fazer por você.*": "Dental care *tailored to you.*",
    "Cada camada do dente, um *cuidado.*": "Every layer deserves *expert care.*",
    "Um especialista para cada *etapa* do seu sorriso.": "Specialists for every *stage* of your smile.",
    "Quem cuida de *você.*": "The people behind *your care.*",
    "Sempre uma unidade *perto de você.*": "Expert care *close to home.*",
    "Onde *estamos.*": "Find us *near you.*",
    "Convênios aceitos": "Accepted insurance plans",
    "Valores de referência": "Treatment pricing",
    "O plano de tratamento e o orçamento final são definidos após a avaliação clínica.": "Treatment plans and final quotes are provided after a clinical consultation.",
    "Conheça o *espaço.*": "Explore our *practice.*",
    "Perguntas *frequentes.*": "Frequently asked *questions.*",
    "Vamos cuidar do seu *sorriso?*": "Ready for a *healthier smile?*",
    "Agendar pelo WhatsApp": "Book via WhatsApp",
    "Falar no WhatsApp": "Chat on WhatsApp",
    "Agendar consulta": "Book an appointment",
    "Agendar avaliação": "Book a consultation",
    "Solicitar horário": "Request an appointment",
    "Solicite seu horário": "Request an appointment",
    "Solicitar pelo WhatsApp": "Request via WhatsApp",
    "Período de preferência": "Preferred time of day",
    "Seu nome completo": "Your full name",
    "Autorizo o contato da clínica sobre este agendamento, conforme a": "I agree to be contacted about this request as outlined in the",
    "Política de Privacidade": "Privacy Policy",
    "Política de privacidade": "Privacy policy",
    "Você envia a mensagem pelo seu WhatsApp. A equipe responde para combinar o horário.": "You send the message through WhatsApp. Our team replies to arrange an appointment.",
    "Sua mensagem está pronta": "Your message is ready",
    "Abrimos o WhatsApp —": "We opened WhatsApp —",
    "em uma nova aba. Envie a mensagem": "in a new tab. Send your message",
    "por lá; o horário ainda": "there; the appointment is",
    "não está confirmado": "not yet confirmed",
    "até a equipe responder.": "until our team replies.",
    "Abrir o WhatsApp novamente": "Open WhatsApp again",
    "Editar solicitação": "Edit request",
    "Role para conhecer": "Scroll to explore",
    "Role para abrir": "Scroll to explore",
    "Cuidados relacionados": "Related treatments",
    "Destaques ilustrativos. O diagnóstico e a indicação de tratamento dependem de avaliação clínica.": "Illustrations only. Diagnosis and treatment recommendations require an individual clinical assessment.",
    "Conheça os especialistas": "Meet our specialists",
    "Ver todos os tratamentos": "View all treatments",
    "Ver equipe completa": "Meet the full team",
    "Como chegar": "Get directions",
    "abre em nova aba": "opens in a new tab",
    "WhatsApp da unidade": "Location WhatsApp",
    "Escolha a": "Choose a",
    "Cada unidade tem o próprio WhatsApp.": "Each location has its own WhatsApp contact.",
    "Demonstração do": "Demo of the",
    "Neste site de demonstração o número de WhatsApp ainda é um placeholder. Na clínica real,": "In this demo, the WhatsApp number is a placeholder. For a real practice,",
    "este botão abre a conversa com a mensagem abaixo já preenchida.": "this button opens a chat with the prefilled message below.",
    "Todos os tratamentos": "All treatments",
    "Página não encontrada": "Page not found",
    "A página procurada não existe.": "The page you requested could not be found.",
    "Esta página *não existe.*": "This page *does not exist.*",
    "O endereço pode ter mudado. Volte ao início ou veja os tratamentos.": "The page may have moved. Return home or explore our treatments.",
    "Voltar ao início": "Back to home",
    "Ver tratamentos": "Browse treatments",
    "Contato e agendamento": "Contact and appointments",
    "Solicite seu horário na": "Request an appointment at",
    "Tratamentos odontológicos oferecidos pela": "Dental treatments available at",
    "Corpo clínico da": "The dental team at",
    "Endereços, horários e WhatsApp das unidades da": "Addresses, opening hours and WhatsApp contacts for",
    "Horários e WhatsApp da unidade.": "Opening hours and contact information.",
    "Cada tratamento começa por uma avaliação completa. Conheça os cuidados oferecidos e fale com a equipe para tirar dúvidas.": "Every treatment starts with a thorough consultation. Explore our services and contact the team with any questions.",
    "Sobre o tratamento": "About this treatment",
    "Duração aproximada:": "Estimated duration:",
    "Como funciona": "What to expect",
    "Quando é indicado": "When it may help",
    "Quem acompanha": "Your care team",
    "Conteúdo informativo. A indicação de qualquer tratamento depende de avaliação clínica individual.": "General information only. Treatment recommendations require an individual clinical assessment.",
    "Texto de exemplo do template: deve ser revisado pelo responsável técnico da clínica.": "Example template content. Review with the practice's licensed clinician before publication.",
    "Dúvidas sobre o *tratamento.*": "Questions about *this treatment.*",
    "Outros tratamentos": "Other treatments",
    "Próximo tratamento": "Next treatment",
    "Tirar dúvidas": "Ask a question",
    "Gostaria de saber mais sobre": "I'd like to learn more about",
    "e agendar uma avaliação.": "and arrange a consultation.",
    "Olá! Gostaria de agendar uma avaliação para": "Hello! I'd like to book a consultation for",
    "Olá! Gostaria de agendar uma consulta com": "Hello! I'd like to book an appointment with",
    "Olá! Gostaria de agendar na": "Hello! I'd like to book an appointment at",
    "A equipe responde pelo WhatsApp para combinar o melhor horário.": "Our team will reply on WhatsApp to arrange a convenient appointment.",
    "Outras formas de contato": "Other ways to contact us",
    "Responsável técnico:": "Licensed clinical lead:",
    "Site de demonstração do template. Os dados entre [colchetes] são fictícios e devem ser": "Demo website. Details in [brackets] are illustrative and must be",
    "substituídos por informações reais e revisadas da clínica.": "replaced with verified practice information before publication.",
    "Ver perfil": "View profile",
    "Tratamentos relacionados": "Related treatments",
    "Atende em": "Practices at",
    "Responsabilidade técnica": "Professional credentials",
    "Unidade principal": "Main location",
    "Onde estamos": "Find us",
    "Módulo opcional · filiais": "Optional feature · locations",
    "Módulo opcional": "Optional section",
    "Unidade única": "Single location",
    "Fotos da clínica": "Dental practice photos",
    "Agendamento rápido": "Quick appointment request",
    "Progresso da página": "Page progress",
    "Principal (compacto)": "Main navigation (compact)",
    "Trilha de navegação": "Breadcrumb navigation",
    "Abrir menu": "Open menu",
    "Fechar menu": "Close menu",
    "Depoimento anterior": "Previous testimonial",
    "Próximo depoimento": "Next testimonial",
    "Destino configurado: WhatsApp": "WhatsApp destination",
    "Informe seu nome.": "Please enter your name.",
    "Digite um nome válido.": "Please enter a valid name.",
    "Escolha a unidade.": "Please choose a location.",
    "Escolha um período.": "Please choose a preferred time.",
    "Para continuar, autorize o contato sobre este agendamento.": "Please agree to be contacted about your appointment request.",
    "Revise o campo destacado.": "Please check the highlighted field.",
    "campos destacados.": "highlighted fields.",
    "Revise os": "Please check the",
    "Mensagem preparada (demonstração).": "Message prepared (demo).",
    "Abrimos o WhatsApp": "We opened WhatsApp",
    "em uma nova aba.": "in a new tab.",
    "Fico no aguardo para combinarmos o melhor horário.": "I look forward to arranging a convenient time.",
    "Gostaria de solicitar um horário.": "I'd like to request an appointment.",
    "Gostaria de saber mais e solicitar um horário para": "I'd like to learn more and request an appointment for",
    "Olá! Meu nome é": "Hello! My name is",
    "Olá!": "Hello!",
    "Camada externa, a mais dura do corpo. Protege o dente no contato com alimentos e na mastigação.": "The hardest substance in the body, enamel protects the outer surface of a tooth.",
    "A dentina sustenta o esmalte e protege a polpa, onde ficam os nervos e vasos que nutrem o dente.": "Dentin supports enamel and protects the pulp, which contains nerves and blood vessels.",
    "Fica abaixo da gengiva e fixa o dente ao osso.": "Below the gumline, the root anchors the tooth to the jawbone.",
    "Camada externa, a mais dura do corpo.": "The outer layer and the hardest substance in the body.",
    "Nervos e vasos que nutrem o dente.": "Nerves and blood vessels that nourish the tooth.",
    "Sustenta o esmalte e protege a polpa.": "Supports enamel and protects the pulp.",
    "Fixa o dente ao osso.": "Anchors the tooth to the jawbone.",
    "Camadas do dente": "Layers of a tooth",
    "Estruturas do dente": "Tooth anatomy",
    "Política de *Privacidade*": "*Privacy* Policy",
    "Atualizada em": "Last updated on",
    "Trilha de navegação": "Breadcrumb navigation",
    "Falar pelo WhatsApp": "Talk on WhatsApp",
}

# Only replace standalone UI labels in string literals and visible HTML text; do
# not rename Astro component imports, TypeScript symbols or internal section IDs.
WORDS = {
    "Início": "Home", "Tratamentos": "Treatments", "Tratamento": "Treatment",
    "Especialidades": "Specialties", "Especialidade": "Specialty",
    "Equipe": "Team", "Corpo clínico": "Dental team", "A clínica": "About us",
    "Clínica": "Practice", "Unidades": "Locations", "Unidade": "Location",
    "Convênios": "Insurance", "Valores": "Pricing", "Depoimentos": "Testimonials",
    "Galeria": "Gallery", "Dúvidas": "FAQs", "Agendamento": "Appointments",
    "Contato": "Contact", "Agendar": "Book now", "Ligar": "Call",
    "Nome": "Name", "Interesse": "Reason for visit", "Período": "Time of day",
    "Motivo": "Reason", "Telefone": "Phone", "E-mail": "Email",
    "Horários": "Opening hours", "Observação": "Note", "Sobre": "About",
    "Esmalte": "Enamel", "Polpa": "Pulp", "Dentina": "Dentin",
    "Raiz": "Root", "Dentina e polpa": "Dentin and pulp",
    "Recepção": "Reception", "Consultório": "Treatment room",
    "Odontologia": "Dentistry", "Ortodontia": "Orthodontics",
    "Implantodontia": "Dental implants", "Endodontia": "Endodontics",
    "Periodontia": "Periodontics", "Odontopediatria": "Pediatric dentistry",
    "Estética e prótese": "Cosmetic & restorative dentistry",
    "Limpeza": "Teeth cleaning", "Restaurações": "Fillings",
    "Próteses": "Prosthetics", "Clareamento": "Teeth whitening",
    "Unidade Centro": "Downtown practice",
    "Unidade Jardins": "Garden practice",
}

DEMO = {
    "Alva Odontologia — demonstração do template": "Alva Dental — website demo",
    "Clínica odontológica com avaliação completa, plano de tratamento explicado com clareza e acompanhamento do primeiro atendimento à manutenção.": "Modern dental care with comprehensive assessments, clear treatment plans and supportive follow-up.",
    "Alva Odontologia": "Alva Dental",
    "Clínica odontológica · [Bairro, Cidade]": "Modern dentistry · [Neighborhood, City]",
    "O cuidado que\\nfica no seu *sorriso.*": "Thoughtful care for\\nyour *best smile.*",
    "Avaliação completa, plano de tratamento explicado com clareza e uma equipe que acompanha você do primeiro atendimento à manutenção.": "Comprehensive consultations, personalized treatment plans and a welcoming team by your side at every step.",
    "Seg a sex [8h–20h] · Sáb [8h–13h] · [Atendemos convênios e particular]": "Mon–Fri [8 am–8 pm] · Sat [8 am–1 pm] · [Insurance and self-pay patients welcome]",
    "Avaliação e prevenção": "Dental checkups & prevention",
    "Consulta completa para entender sua saúde bucal e planejar os próximos passos.": "A complete dental checkup to understand your oral health and plan next steps.",
    "A avaliação é o ponto de partida de qualquer tratamento. O dentista examina dentes, gengiva, mordida e tecidos da boca e conversa com você sobre queixas, hábitos e histórico de saúde.": "A dental examination is the starting point for any treatment. Your dentist assesses your teeth, gums, bite and oral tissues, and discusses your concerns, habits and medical history.",
    "Quando necessário, solicita exames de imagem. Ao final, você recebe um plano explicado em linguagem clara, com prioridades e alternativas.": "If needed, the dentist may recommend imaging. You will receive a clearly explained treatment plan with priorities and available options.",
    "Conversa inicial": "Initial conversation",
    "Histórico de saúde, queixas e expectativas.": "Medical history, concerns and expectations.",
    "Exame clínico": "Clinical examination",
    "Dentes, gengiva, mordida e tecidos moles.": "Teeth, gums, bite and soft tissues.",
    "Plano de tratamento": "Treatment plan",
    "Prioridades, alternativas e próximos passos.": "Priorities, options and next steps.",
    "Remoção de placa e tártaro com orientação de higiene para o dia a dia.": "Professional plaque and tartar removal, plus tailored oral hygiene guidance.",
    "A limpeza profissional (profilaxia) remove a placa bacteriana e o tártaro que a escovação não alcança, sobretudo perto da gengiva e entre os dentes.": "Professional cleaning removes plaque and tartar that brushing alone cannot remove, particularly along the gumline and between the teeth.",
    "Na mesma consulta, a equipe revisa sua técnica de escovação e o uso do fio dental. A frequência das limpezas é definida pelo dentista conforme sua necessidade.": "Your dental team can also review brushing and flossing techniques. Your dentist will recommend a cleaning schedule suited to your needs.",
    "Clareamento dental supervisionado pelo dentista, após avaliação.": "Professional teeth whitening supervised by a dentist following an examination.",
    "O clareamento usa géis específicos para clarear a cor dos dentes. Antes de começar, o dentista verifica se há cáries, sensibilidade ou restaurações que mudem a indicação.": "Teeth whitening uses specially formulated gels to lighten tooth color. Before treatment, your dentist checks for decay, sensitivity and existing restorations.",
    "A técnica (em consultório, caseira supervisionada ou combinada) é escolhida caso a caso. Restaurações e próteses não clareiam e podem precisar de ajuste depois.": "In-office, professionally supervised at-home or combined options may be recommended. Fillings and crowns do not whiten and may require adjustment afterward.",
    "Recuperação da forma e da função de dentes com cárie ou fraturas.": "Restore the shape and function of teeth affected by cavities or damage.",
    "A restauração remove a parte comprometida do dente e reconstrói a região com materiais da cor do dente, devolvendo forma e função para a mastigação.": "A filling replaces damaged tooth structure with a tooth-colored material to restore shape and chewing function.",
    "Quando o desgaste é maior, o dentista pode indicar restaurações indiretas, produzidas fora da boca e cimentadas em uma segunda consulta.": "For extensive damage, your dentist may recommend a custom inlay or onlay made outside the mouth and bonded in place.",
    "Lentes e facetas": "Dental veneers",
    "Lâminas que alteram cor, forma ou alinhamento aparente dos dentes da frente.": "Thin custom shells that improve the color, shape or appearance of front teeth.",
    "Lentes de contato dental e facetas são lâminas finas, geralmente de cerâmica ou resina, aplicadas na face visível dos dentes para corrigir cor, forma e pequenos espaços.": "Veneers are thin porcelain or composite shells applied to the visible surface of teeth to improve color, shape and small gaps.",
    "O planejamento inclui avaliação da mordida e da gengiva e, muitas vezes, um ensaio do resultado antes do tratamento definitivo.": "Planning includes an assessment of your bite and gums and may include a preview of the expected result.",
    "Tratamento de canal": "Root canal treatment",
    "Tratamento da polpa para aliviar a dor e preservar o dente natural.": "Treat the dental pulp to relieve discomfort and help preserve your natural tooth.",
    "Quando a polpa — o tecido com nervos e vasos dentro do dente — inflama ou infecciona, o tratamento de canal limpa, desinfeta e veda o interior do dente.": "When the tooth pulp becomes inflamed or infected, root canal treatment cleans, disinfects and seals the inner canals.",
    "O objetivo é manter o dente natural na boca. Depois do canal, o dente costuma precisar de uma restauração ou coroa para ficar protegido.": "The goal is to save your natural tooth. A filling or crown may be needed afterward to protect it.",
    "Reposição de dentes perdidos com implantes, do planejamento à manutenção.": "Replace missing teeth with implants, from planning through long-term care.",
    "O implante é um pino, geralmente de titânio, instalado no osso para substituir a raiz de um dente perdido. Sobre ele é fixada uma coroa ou prótese.": "A dental implant is a small post, usually made of titanium, placed in the jawbone to replace a missing tooth root and support a crown or other restoration.",
    "O planejamento avalia a quantidade de osso, a saúde da gengiva e as condições gerais de saúde. Prazos e etapas variam de caso para caso.": "Planning considers jawbone volume, gum health and your overall health. Treatment stages and timelines vary by patient.",
    "Coroas, pontes e próteses para reabilitar dentes desgastados ou ausentes.": "Crowns, bridges and dentures to restore damaged or missing teeth.",
    "Próteses dentárias repõem dentes ausentes ou reconstroem dentes muito desgastados. Podem ser fixas (coroas e pontes), removíveis ou apoiadas sobre implantes.": "Dental prosthetics replace missing teeth or rebuild heavily worn teeth. Options include crowns, bridges, removable dentures and implant-supported restorations.",
    "A escolha depende da quantidade de dentes envolvidos, da saúde da gengiva e do osso e das preferências de cada paciente.": "Your options depend on the teeth involved, gum and bone health, and your personal preferences.",
    "Aparelhos e alinhadores": "Braces & clear aligners",
    "Correção da posição dos dentes e da mordida com aparelhos ou alinhadores.": "Improve alignment and bite using braces or clear aligners.",
    "A ortodontia corrige a posição dos dentes e a relação entre as arcadas. O tratamento pode usar aparelhos fixos ou alinhadores transparentes removíveis.": "Orthodontic treatment aligns teeth and corrects bite issues using braces or removable clear aligners.",
    "Em crianças e adolescentes, o ortodontista também acompanha o crescimento facial para indicar o melhor momento de intervir.": "For children and teenagers, an orthodontist also monitors facial growth to determine when treatment may be most helpful.",
    "Tratamento de gengiva": "Gum disease treatment",
    "Prevenção e controle da inflamação e do sangramento gengival.": "Prevent and manage gum inflammation and bleeding.",
    "Sangramento, inchaço e retração da gengiva podem indicar doença periodontal. O tratamento inclui raspagem para remover o tártaro abaixo da gengiva e acompanhamento.": "Bleeding, swelling and receding gums may indicate periodontal disease. Care may include deep cleaning below the gumline and regular follow-up.",
    "Manter a gengiva saudável protege o osso que sustenta os dentes e é parte importante do planejamento de outros tratamentos.": "Healthy gums help protect the bone supporting your teeth and are essential to many other dental treatments.",
    "Aparelhos fixos, alinhadores transparentes e acompanhamento do crescimento facial.": "Braces, clear aligners and orthodontic growth monitoring.",
    "Tratamento de canal para aliviar a dor e preservar o dente natural.": "Root canal therapy to ease discomfort and preserve natural teeth.",
    "Saúde da gengiva: prevenção, raspagem e controle de sangramentos.": "Gum health, preventive care and treatment for inflammation and bleeding.",
    "Atendimento acolhedor para bebês, crianças e adolescentes.": "Gentle dental care for infants, children and teenagers.",
    "Lentes de contato dental, clareamento e reabilitação do sorriso.": "Veneers, teeth whitening and smile restoration.",
    "Um espaço pensado para o seu *conforto.*": "A welcoming space designed *around you.*",
    "[Texto curto sobre a história da clínica, o jeito de atender e o que diferencia a experiência do paciente.]": "[Tell your practice's story and what makes the patient experience special.]",
    "[Esterilização com rastreio por paciente]": "[Documented instrument sterilization procedures]",
    "[Acesso para cadeirantes]": "[Wheelchair accessible]",
    "[Estacionamento conveniado]": "[Convenient parking]",
    "Biossegurança": "Patient safety", "Acessibilidade": "Accessibility", "Comodidade": "Convenience",
    "[Foto real — recepção]": "[Real photo — reception]",
    "[Foto real — consultório]": "[Real photo — treatment room]",
    "[Foto real — fachada]": "[Real photo — exterior]",
    "[Foto real — sala de espera]": "[Real photo — waiting area]",
    "[Foto real — esterilização]": "[Real photo — sterilization area]",
    "Recepção da clínica": "Practice reception",
    "Recepção · Unidade Centro": "Reception · Downtown practice",
    "Sala de espera": "Waiting room",
    "Área de esterilização": "Sterilization area", "Esterilização": "Sterilization",
    "Dra. [Nome Sobrenome]": "Dr. [Full Name]",
    "Dr. [Nome Sobrenome]": "Dr. [Full Name]",
    "[Biografia breve: formação, áreas de atuação e jeito de atender, escrita e aprovada pelo profissional.]": "[Short clinician-approved bio: education, areas of expertise and approach to patient care.]",
    "[Biografia breve aprovada pelo profissional.]": "[Short biography approved by the clinician.]",
    "[Graduação — Instituição, ano]": "[Degree — University, year]",
    "[Especialização — Instituição, ano]": "[Specialty training — Institution, year]",
    "Unidade Centro": "Downtown practice", "Centro": "Downtown",
    "Unidade Jardins": "Garden practice", "Jardins": "Garden",
    "[Unidade 3]": "[Location 3]",
    "[Rua]": "[Street]", "[número]": "[Number]", "[Bairro]": "[Neighborhood]",
    "[Cidade]": "[City]", "[UF]": "[State]",
    "Seg a sex": "Mon–Fri", "Sáb": "Sat",
    "[8h–20h]": "[8 am–8 pm]", "[8h–19h]": "[8 am–7 pm]",
    "[9h–18h]": "[9 am–6 pm]", "[8h–13h]": "[8 am–1 pm]",
    "[WhatsApp da Unidade Centro]": "[Downtown WhatsApp number]",
    "[WhatsApp da Unidade Jardins]": "[Garden WhatsApp number]",
    "[WhatsApp da Unidade 3]": "[Location 3 WhatsApp number]",
    "[Estacionamento no local]": "[On-site parking]",
    "[Observação]": "[Additional information]",
    "Também atendemos particular. [Condições de pagamento.]": "Self-pay patients are welcome. [Payment information.]",
    "Consulta de avaliação": "Dental consultation", "Limpeza e profilaxia": "Professional cleaning",
    "Implante unitário": "Single dental implant", "sob avaliação": "Price on consultation",
    "a partir de": "from",
    "[Trecho de uma avaliação real de paciente sobre o atendimento, publicada com autorização — até duas linhas. Exemplo": "[Excerpt of a genuine patient review published with written permission. Example",
    "[Nome do paciente]": "[Patient name]", "Avaliação no Google": "Google review",
    "Como funciona a primeira consulta?": "What happens at my first appointment?",
    "[Descreva a primeira consulta na clínica: duração, exames e o que o paciente deve levar.]": "[Describe what happens at the first appointment, how long it takes and what patients should bring.]",
    "Vocês atendem convênios?": "Do you accept dental insurance?",
    "[Liste os convênios aceitos e como confirmar a cobertura.]": "[List accepted insurance plans and how to confirm coverage.]",
    "Atendem urgências?": "Do you offer emergency dental care?",
    "[Explique como funciona o atendimento de urgência e os horários.]": "[Explain emergency availability and how to request urgent dental care.]",
    "Escolha a unidade e o melhor período. A equipe confirma o horário com você pelo WhatsApp.": "Choose a location and your preferred time of day. Our team will confirm the appointment with you on WhatsApp.",
    "Escolha o melhor período. A equipe confirma o horário com você pelo WhatsApp.": "Choose your preferred time of day. Our team will confirm the appointment with you on WhatsApp.",
    "Primeira avaliação": "New patient consultation", "Dor ou urgência": "Tooth pain or emergency",
    "Implantes": "Dental implants", "Outro assunto": "Other",
    "Manhã": "Morning", "Tarde": "Afternoon", "Noite": "Evening",
    "[Razão social]": "[Registered business name]",
    "[data]": "[date]", "[Dr(a). Nome]": "Dr. [Full Name]",
    "Dr(a). [Nome]": "Dr. [Full Name]",
    "CRO-[UF] [00000]": "[Professional license number]",
    "CRO-[UF] 00000": "[Professional license number]",
    "[00.000.000/0000-00]": "[Business registration number]",
    "[R$ 000]": "[Price]",
    "[contato@clinica.com.br]": "[hello@example-dental.com]",
    "[privacidade@clinica.com.br]": "[privacy@example-dental.com]",
}
# Slugs are URL identifiers. Keep internal specialty/team IDs unchanged.
SLUGS = {
    "avaliacao-e-prevencao": "checkups-and-prevention",
    "limpeza": "teeth-cleaning",
    "clareamento": "teeth-whitening",
    "restauracoes": "dental-fillings",
    "lentes-e-facetas": "dental-veneers",
    "tratamento-de-canal": "root-canal-treatment",
    "implantes": "dental-implants",
    "proteses": "crowns-and-dentures",
    "aparelhos-e-alinhadores": "braces-and-aligners",
    "tratamento-de-gengiva": "gum-disease-treatment",
}
PAGE_MOVES = {
    "src/pages/a-clinica.astro": "src/pages/about.astro",
    "src/pages/contato.astro": "src/pages/contact.astro",
    "src/pages/privacidade.astro": "src/pages/privacy.astro",
    "src/pages/equipe/[...slug].astro": "src/pages/team/[...slug].astro",
    "src/pages/unidades/[...slug].astro": "src/pages/locations/[...slug].astro",
    "src/pages/tratamentos/index.astro": "src/pages/treatments/index.astro",
    "src/pages/tratamentos/[slug].astro": "src/pages/treatments/[slug].astro",
}

def replace_pairwise(src, mapping):
    for pt, en in sorted(mapping.items(), key=lambda item: -len(item[0])):
        src = src.replace(pt, en.replace("'", "’"))
    return src

def localize_ui(src):
    src = replace_pairwise(src, PHRASES)
    for pt, en in sorted(WORDS.items(), key=lambda item: -len(item[0])):
        src = src.replace("'" + pt + "'", "'" + en + "'")
        src = src.replace('"' + pt + '"', '"' + en + '"')
        # Preserve indentation around plain text labels inside HTML.
        src = re.sub(r">(\s*)" + re.escape(pt) + r"(\s*)<",
                     lambda m: ">" + m.group(1) + en + m.group(2) + "<", src)
    src = replace_pairwise(src, ROUTES)
    src = src.replace('lang="pt-BR"', 'lang="en"').replace('content="pt_BR"', 'content="en_US"')
    return src

def localized_privacy():
    return """---
import BaseLayout from '@/layouts/BaseLayout.astro';
import PageHeader from '@/components/layout/PageHeader.astro';
import site, { siteUrl } from '@/lib/site';
import { breadcrumbLd } from '@/lib/seo';
const { c } = site.c ? { c: site.c } : { c: site.c };
const base = siteUrl();
const privacy = c.legal.encarregado;
---
<BaseLayout path="/privacy/" title="Privacy Policy"
  description={\u0060How \u0024{c.marca.nome} handles information provided through this website.\u0060}
  jsonLd={[breadcrumbLd([{ nome: 'Home', url: \u0060\u0024{base}/\u0060 }, { nome: 'Privacy Policy', url: \u0060\u0024{base}/privacy/\u0060 }])]}>
  <div class="container page">
    <PageHeader trilha={[{ nome: 'Home', href: '/' }, { nome: 'Privacy Policy' }]}
      rotulo="Privacy" titulo="Our *Privacy Policy*" />
    <div class="legal">
      <p>This is a customizable privacy notice for a demonstration dental website. It is not a substitute for legal review under the laws of the country or state in which the practice operates.</p>
      <h2>1. About this practice</h2>
      <p>This site is provided by {c.legal.razaoSocial}, business registration {c.legal.cnpj}. Clinical lead: {c.legal.responsavelTecnico.nome} ({c.legal.responsavelTecnico.cro}).</p>
      <h2>2. Information you provide</h2>
      <p>The website does not require you to create an account. When you fill in an appointment request, your name, preferred location, reason for visiting and preferred time of day are assembled into a WhatsApp message on your device. <strong>The website itself does not submit or store this message.</strong> The practice receives it only if you choose to send it through WhatsApp.</p>
      <p>Please do not submit detailed medical or other sensitive information through the appointment form. Discuss clinical concerns directly with the practice.</p>
      <h2>3. How information is used</h2>
      <p>The practice may use the information you send to respond to your request, arrange appointments and manage communications. Local privacy requirements and lawful bases for processing must be confirmed by the practice before launch.</p>
      <h2>4. Third-party services</h2>
      <p>Appointment requests may open WhatsApp, a service operated by Meta and subject to its own privacy terms. This template does not include third-party advertising trackers. Confirm any additional integrations before publication.</p>
      <h2>5. Your choices</h2>
      <p>You can contact the practice to ask how it handles, accesses, corrects or deletes information you have provided, subject to applicable local law and clinical record-retention obligations.</p>
      <h2>6. Contact</h2>
      <p>{privacy?.nome ? privacy.nome + ' — ' : ''}{privacy?.email ? (privacy.email.includes('[') ? privacy.email : <a href={\u0060mailto:\u0024{privacy.email}\u0060}>{privacy.email}</a>) : 'Contact the practice through the listed contact options.'}</p>
      {site.demo && <p class="legal__demo">Demo only. Replace all bracketed placeholders and obtain local legal review before using this policy for a real practice.</p>}
    </div>
  </div>
</BaseLayout>
"""

def main():
    changed = []
    for file in list((ROOT / "src").rglob("*.astro")) + list((ROOT / "src").rglob("*.ts")):
        relative = file.relative_to(ROOT).as_posix()
        # Do not modify technical IDs or fixture data; main demo receives custom translations.
        if relative.startswith("src/clients/") or relative.startswith("src/config/") or relative.startswith("src/pages/privacy."):
            continue
        original = file.read_text(encoding="utf-8")
        new = localize_ui(original)
        dest = ROOT / PAGE_MOVES.get(relative, relative)
        if relative == "src/pages/privacidade.astro":
            new = localized_privacy()
        if dest != file or new != original:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(new, encoding="utf-8")
            if dest != file:
                file.unlink()
            changed.append(dest.relative_to(ROOT).as_posix())

    file = ROOT / "src/clients/alva-demo/clinic.ts"
    content = file.read_text(encoding="utf-8")
    content = replace_pairwise(content, DEMO)
    content = localize_ui(content)
    for a, b in SLUGS.items():
        content = content.replace("slug: '" + a + "'", "slug: '" + b + "'")
    # New markets should use neutral contact, credentials and geography examples.
    content = content.replace("https://alva-odontologia-demo.vercel.app", "https://example-dental-practice.com")
    content = content.replace("CRO-[State]", "[Professional license number]")
    content = content.replace("[(00) 0000-0000]", "[+1 (000) 000-0000]")
    file.write_text(content, encoding="utf-8")
    changed.append(file.relative_to(ROOT).as_posix())

    # English defaults for new client installations without changing schema field names.
    config = ROOT / "src/config/clinic.schema.ts"
    content = config.read_text(encoding="utf-8")
    content = localize_ui(content)
    content = content.replace("Olá! Gostaria de agendar uma avaliação.", "Hello! I'd like to book a dental consultation.")
    config.write_text(content, encoding="utf-8")
    changed.append(config.relative_to(ROOT).as_posix())
    template = ROOT / "src/clients/_modelo/clinic.ts"
    content = template.read_text(encoding="utf-8")
    content = localize_ui(content)
    content = replace_pairwise(content, DEMO)
    content = content.replace("https://www.dominio-da-clinica.exemplo", "https://www.your-dental-practice.com")
    template.write_text(content, encoding="utf-8")
    changed.append(template.relative_to(ROOT).as_posix())

    pkg = ROOT / "package.json"
    content = pkg.read_text(encoding="utf-8")
    content = content.replace('"name": "alva-template-odontologia"', '"name": "alva-dental-template-en"')
    content = content.replace("Template comercial reutilizável para sites de clínicas odontológicas brasileiras (identidade de demonstração: Alva Odontologia).",
                              "Professional English-language website template for international dental practices.")
    pkg.write_text(content, encoding="utf-8")
    changed.append("package.json")

    # No false country information in schema.org. Country is configurable per location.
    seo = ROOT / "src/lib/seo.ts"
    content = seo.read_text(encoding="utf-8")
    content = content.replace("addressCountry: 'BR',", "addressCountry: (e as typeof e & { pais?: string }).pais || 'US',")
    seo.write_text(content, encoding="utf-8")
    changed.append("src/lib/seo.ts")
    README = ROOT / "README.md"
    README.write_text("""# Alva Dental — English Website Template

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

Edit the generated file in \u0060src/clients/customer-name/clinic.ts\u0060. The internal schema names remain Portuguese for compatibility with the original implementation; **visitor-facing copy is English**.

### International launch checklist

- Replace every placeholder with verified clinic, clinician, licensing and contact information.
- Update the practice country, currency, opening hours, phone country codes and payment methods.
- Review the privacy notice and all professional advertising statements under applicable **local** law.
- Configure \u0060SITE_URL\u0060 for the real domain and check metadata, canonical URLs and structured data.
- Do not assume an appointment has been booked: the WhatsApp flow only sends an inquiry.
- Confirm the preferred contact method for each market. WhatsApp is available as a starting point, but additional contact integrations may be useful.

## Structure

The template keeps independent configurable sections for treatments, specialties, team, locations, insurance, testimonials, gallery, FAQ and appointment requests. English public routes include \u0060/treatments/\u0060, \u0060/team/\u0060, \u0060/locations/\u0060, \u0060/about/\u0060, \u0060/contact/\u0060 and \u0060/privacy/\u0060. The source template remains unchanged.
""", encoding="utf-8")
    changed.append("README.md")
    print("Localized " + str(len(changed)) + " files:")
    for f in changed: print("  " + f)


def finalize():
    """Polish residual Portuguese labels and set international defaults."""
    fixes = {
        "src/components/forms/BookingForm.astro": {"</a> (LGPD).": "</a>."},
        "src/components/navigation/Dialogs.astro": {
            'Choose a <em class="destaque">unidade</em>': 'Choose a <em class="destaque">location</em>',
            'aria-label="Fechar"': 'aria-label="Close"',
            "        Entendi": "        Got it",
        },
        "src/components/layout/Footer.astro": {"· CNPJ {legal.cnpj}": "· Business ID {legal.cnpj}"},
        "src/components/sections/Agendamento.astro": {"'Endereço'": "'Address'"},
        "src/components/sections/Unidades.astro": {
            " à {u.nome}": " for {u.nome}",
            "WhatsApp da " + "$" + "{u.nome}": "WhatsApp for " + "$" + "{u.nome}",
        },
        "src/components/sections/Equipe.astro": {
            "Sobre <Icon": "About <Icon",
            "join(' e ')": "join(' and ')",
        },
        "src/pages/about.astro": {"· CNPJ {c.legal.cnpj}": "· Business ID {c.legal.cnpj}"},
        "src/pages/team/[...slug].astro": {
            "join(' e ')": "join(' and ')",
            'texto="Formação"': 'texto="Education & qualifications"',
        },
        "src/pages/locations/[...slug].astro": {'texto="Quem atende nesta unidade"': 'texto="Clinicians at this location"'},
        "src/components/cinema/EspecialidadesPanel.astro": {
            "Conheça " + "$" + "{comPagina.nome}": "Meet " + "$" + "{comPagina.nome}",
            "Saiba mais sobre " + "$" + "{trat.nome.toLowerCase()}": "Learn more about " + "$" + "{trat.nome.toLowerCase()}",
        },
        "src/pages/treatments/[slug].astro": {
            "Tratamento · " + "$" + "{especialidade.nome}": "Treatment · " + "$" + "{especialidade.nome}",
        },
        "src/lib/whatsapp.ts": {
            "• Unidade:": "• Location:",
            "• Interesse:": "• Reason for visit:",
            "• Período de preferência:": "• Preferred time:",
        },
        "src/scripts/ui/forms.ts": {
            "Unidade " + "$" + "{unidade.nome}": "Location " + "$" + "{unidade.nome}",
            ".replace(/^Unidade Unidade/, 'Location')": "",
        },
        "src/clients/alva-demo/clinic.ts": {
            "[Logo convênio " + "$" + "{i + 1}]": "[Insurance logo " + "$" + "{i + 1}]",
        },
        "src/lib/seo.ts": {
            "addressCountry: (e as typeof e & { pais?: string }).pais || 'US',":
            "addressCountry: e.pais || 'US',",
        },
        "src/config/clinic.schema.ts": {
            "  uf: z.string(),\n  cep:": "  uf: z.string(),\n  /** Country code: US, GB, CA, AU, etc. */\n  pais: z.string().length(2).default('US'),\n  cep:",
        },
        "src/clients/_modelo/clinic.ts": {
            "[Nome da Clínica]": "[Practice Name]",
            "[nome]": "[brand]",
            "Odontologia em": "Dental Care in",
            "[(00) 0000-0000]": "[+1 000 000 0000]",
            "[55DDD000000000]": "[International WhatsApp number]",
            "[Descrição curta da clínica para buscadores, até ~155 caracteres.]":
                "[Brief, accurate practice description for search engines.]",
            "[Frase de apresentação da clínica.]": "[A welcoming introduction to your practice.]",
            "nome: 'Avaliação'": "nome: 'Dental checkup'",
            "slug: 'avaliacao'": "slug: 'dental-checkup'",
            "[Uma frase sobre a avaliação.]": "[One sentence about the consultation.]",
            "[Texto próprio sobre a avaliação, revisado pelo responsável técnico.]":
                "[Clinician-reviewed copy about the consultation.]",
            "[Nome da unidade]": "[Practice Location]",
            "[Rua]": "[Street]", "[número]": "[Number]",
            "[Bairro]": "[Neighborhood]", "[Cidade]": "[City]", "[UF]": "[State]",
            "Seg a sex": "Mon–Fri", "[8h–18h]": "[9 am–6 pm]",
            "[CRO-UF 00000]": "[Professional license number]",
            "[Razão social]": "[Registered business name]",
        },
    }
    for relative, mapping in fixes.items():
        file = ROOT / relative
        if file.exists():
            src = file.read_text(encoding="utf-8")
            new = src
            for a, b in sorted(mapping.items(), key=lambda item: -len(item[0])):
                new = new.replace(a, b)
            if new != src:
                file.write_text(new, encoding="utf-8")
                print("Polished", relative)
    privacy = ROOT / "src/pages/privacy.astro"
    src = privacy.read_text(encoding="utf-8")
    src = src.replace("const { c } = site.c ? { c: site.c } : { c: site.c };", "const { c } = site;")
    if "<style>" not in src:
        src += """
<style>
  .page { padding-right: var(--gutter-r); padding-bottom: var(--section-gap); }
  .legal { margin-top: 56px; max-width: 720px; }
  .legal h2 { margin-top: 44px; font-family: var(--f-serif); font-size: 28px; line-height: 1.15; }
  .legal p { margin-top: 14px; font-size: 16px; line-height: 1.7; color: var(--c-ink-2); }
  .legal__demo { padding: 12px 16px; border: 1px dashed var(--c-line-strong); border-radius: 12px; color: var(--c-muted) !important; }
  @media (max-width: 899px) { .page { padding-right: var(--gutter); } }
</style>
"""
    privacy.write_text(src, encoding="utf-8")
    print("Polished privacy page")

if __name__ == "__main__":
    main()
    finalize()
