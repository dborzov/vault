update 
       courier 
    set
       id="In-House Driver"
datatype    where 
       name="In-House Driver";


insert into image (id, url_src) values ("41","https://s3.amazonaws.com/sowingo_dev/dental_mart_logo.jpg");

select
    o.id                 as id,
    o.id                 as order_id,
    substring(o.id,1,8)  as order_no,
    max(o.shipment_type) as shipping_method,
    max(os.name)         as status,
    max(o.total)         as amount,
    max(dp.name)         as customer_account,
    group_concat(distinct ovg.id separator ',')
                         as ovg_ids,
    datediff(max(o.deadline), now())
                         as days_left,
    max(o.created_at)    as order_date,
    max(o.deadline)      as order_deadline
from
    `order` o
    inner join `order_status` os            on os.id = o.status_id
    inner join `order_vendor_group` ovg     on o.id  = ovg.order_id
    left outer join dental_practice dp      on dp.id = o.customer_id
%s
group by
    o.id