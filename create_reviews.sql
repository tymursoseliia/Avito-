-- Create the reviews table
create table public.reviews (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default timezone('utc'::text, now()) not null,
  author_name text not null,
  rating integer not null default 5,
  date_text text not null,
  car_title text not null,
  comment_text text not null,
  comment_photos jsonb default '[]'::jsonb,
  reply_text text,
  reply_photos jsonb default '[]'::jsonb
);

-- Set up Row Level Security (RLS)
alter table public.reviews enable row level security;

-- Create policies for anonymous access (since we are using anon key for now)
create policy "Allow public read access"
  on public.reviews
  for select
  to public
  using (true);

create policy "Allow public insert access"
  on public.reviews
  for insert
  to public
  with check (true);

create policy "Allow public update access"
  on public.reviews
  for update
  to public
  using (true)
  with check (true);

create policy "Allow public delete access"
  on public.reviews
  for delete
  to public
  using (true);
