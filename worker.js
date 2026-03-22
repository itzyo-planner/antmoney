import html from './ant_finance_sim_v2.html';

export default {
  fetch() {
    return new Response(html, {
      headers: { 'content-type': 'text/html;charset=UTF-8' },
    });
  },
};
