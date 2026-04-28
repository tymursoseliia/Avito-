const fs = require('fs');

const html = fs.readFileSync('admin.html', 'utf8');
const scriptMatch = html.match(/<script>(.*?)<\/script>/s);
let script = scriptMatch[1];

const mockDoc = `
const document = {
    getElementById: (id) => ({ id, addEventListener: () => {}, innerHTML: '', textContent: '', value: '', style: {}, childNodes: [{nodeValue: ''}] }),
    querySelectorAll: () => [],
    addEventListener: () => {}
};
const window = { scrollTo: () => {} };
const confirm = () => true;
const supabase = {
    createClient: () => ({
        from: () => ({
            select: () => ({ order: () => Promise.resolve({ data: [ { id: 1, author_name: null, comment_text: null, rating: null, date_text: null, car_title: null } ], error: null }) }),
            update: () => ({ eq: () => Promise.resolve({ error: null }) }),
            delete: () => ({ eq: () => Promise.resolve({ error: null }) }),
            insert: () => Promise.resolve({ error: null })
        }),
        storage: {
            from: () => ({ upload: () => Promise.resolve({ data: {}, error: null }), getPublicUrl: () => ({ data: { publicUrl: 'http://test' } }) })
        }
    })
};
`;

script = mockDoc + script;

try {
    eval(script);
    setTimeout(() => {
        console.log("Async code ran successfully.");
    }, 100);
} catch(e) {
    console.error("ERROR:", e);
}
