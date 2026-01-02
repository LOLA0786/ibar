export class IBarPOS {
  constructor({ baseUrl, token }) {
    this.baseUrl = baseUrl;
    this.token = token;
  }

  async authorizePour({ bottleId, pourMl, qrIssuedAt }) {
    const scanId = crypto.randomUUID();

    const res = await fetch(`${this.baseUrl}/pos/authorize-pour`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${this.token}`,
        "Idempotency-Key": scanId,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        bottle_id: bottleId,
        pour_ml: pourMl,
        qr_issued_at: qrIssuedAt
      })
    });

    if (!res.ok) {
      const err = await res.text();
      return { decision: "BLOCK", reason: err };
    }

    return await res.json();
  }
}
