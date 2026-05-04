-- Create the company_photos table
create table public.company_photos (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  url text not null,
  order_index integer not null default 0
);

-- Set up Row Level Security (RLS)
alter table public.company_photos enable row level security;

-- Create policies for anonymous access (since we are using anon key for now)
create policy "Allow public read access"
  on public.company_photos
  for select
  to public
  using (true);

create policy "Allow public insert access"
  on public.company_photos
  for insert
  to public
  with check (true);

create policy "Allow public update access"
  on public.company_photos
  for update
  to public
  using (true)
  with check (true);

create policy "Allow public delete access"
  on public.company_photos
  for delete
  to public
  using (true);
