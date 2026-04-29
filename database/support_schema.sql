CREATE TABLE tb_tickets_suporte (
    id_ticket SERIAL PRIMARY KEY,
    canal_origem VARCHAR(20), -- Chat, E-mail, Voz
    descricao_problema TEXT,
    prioridade VARCHAR(10) DEFAULT 'Normal',
    data_abertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'Aberto'
);

INSERT INTO tb_tickets_suporte (canal_origem, descricao_problema) 
VALUES ('Chat', 'Erro crítico no processamento do pagamento');
